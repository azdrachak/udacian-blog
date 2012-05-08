import webapp2

import handlers

app = webapp2.WSGIApplication([('/', handlers.MainHandler),
                                ('/birth-date', handlers.BirthDateHandler),
                                ('/thanks', handlers.ThanksHandler),
                                ('/rot13', handlers.Rot13Encryption),
                                ('/signup', handlers.UserSignUp),
                                ('/welcome', handlers.UserWelcome),
                                ('/ascii', handlers.ASCII_Page),
                                ('/blog', handlers.BlogFront),
                                ('/blog/newpost', handlers.NewPost),
                                ('/blog/(\d+)', handlers.PermaLink)],
                              debug=True)
