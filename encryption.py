__author__ = 'Aliaksandr Zdrachak'

import string

caps = list(string.ascii_uppercase)
lows = list(string.ascii_lowercase)

def rot13(text):
    list_text = list(text)
    for i in range(len(list_text)):
        if list_text[i] in caps:
            l_index = caps.index(list_text[i])
            list_text[i] = caps[l_index + 13 - 26] if (l_index + 13 > 25) else caps[l_index + 13]
        if list_text[i] in lows:
            l_index = lows.index(list_text[i])
            list_text[i] = lows[l_index + 13 - 26] if (l_index + 13 > 25) else lows[l_index + 13]
    return ''.join(list_text)
#print rot13('The Quick Brown Fox Jumps Over The Lazy Dog.')