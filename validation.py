__author__ = 'Aliaksandr_Zdrachak'

import cgi
import re

def valid_year(year):
    if year and year.isdigit():
        if int(year) > 1889 and int(year) <= 2020:
            return int(year)

def valid_day(day):
    if day and day.isdigit():
        if int(day) in range(1, 32):
            return int(day)

def valid_month(month):
    months = ['January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']
    month_abbvs = dict((m[:3].lower(), m) for m in months)
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)

def escape_html(s):
    return cgi.escape(s, quote = True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_user(username):
    return USER_RE.match(username)
def valid_pass(password):
    return PASS_RE.match(password)
def valid_mail(email):
    return MAIL_RE.match(email)

