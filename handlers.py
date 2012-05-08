__author__ = 'Aliaksandr_Zdrachak'

import webapp2
import jinja2
import os

from google.appengine.ext import db

jinja_env = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

import forms, validation, encryption

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello to all")


class Rot13Encryption(webapp2.RequestHandler):
    def write_form(self, data = "Type in text to encrypt"):
        self.response.out.write(forms.form_encrypt % {"data": validation.escape_html(data)})

    def get(self):
        self.write_form()

    def post(self):
        to_encrypt = self.request.get("text")
        self.write_form(encryption.rot13(to_encrypt))


class BirthDateHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(forms.form % {'error': error,
                                              'month': validation.escape_html(month),
                                              'day': validation.escape_html(day),
                                              'year': validation.escape_html(year)})

    def get(self):
        #self.response.headers['Content-type'] = 'text/plain'
        self.write_form()

    def post(self):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")

        month = validation.valid_month(user_month.strip(' \t\n\r'))
        day = validation.valid_day(user_day.strip(' \t\n\r'))
        year = validation.valid_year(user_year.strip(' \t\n\r'))

        if not (month and day and year):
            self.write_form("That does not look valid for me, friend",
                user_month, user_day, user_year)
        else:
            self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")


class UserSignUp(webapp2.RequestHandler):
    def write_form(self, username = "",
                        password = "",
                        verify = "",
                        email = "",
                        error_username = "",
                        error_password = "",
                        error_verify = "",
                        error_email = ""):
        self.response.out.write(forms.form_signup % {'username': validation.escape_html(username),
                                                     'password': validation.escape_html(password),
                                                     'verify': validation.escape_html(verify),
                                                     'email': validation.escape_html(email),
                                                     'error_username': error_username,
                                                     'error_password': error_password,
                                                     'error_verify': error_verify,
                                                     'error_email': error_email})

    def get(self):
        self.write_form()

    def post(self):
        entered_username = self.request.get('username')
        entered_password = self.request.get('password')
        entered_verify = self.request.get('verify')
        entered_email = self.request.get('email')

        username = validation.valid_user(entered_username)
        password = validation.valid_pass(entered_password)
        email = validation.valid_mail(entered_email)

        if not (username and password and (entered_password == entered_verify) and email):
            error_username, error_password, error_verify, error_email = '', '', '', ''
            if not username:
                error_username = "That's not a valid username."
            if not password:
                error_password = "That wasn't a valid password."
            if entered_password != entered_verify:
                error_verify = "Your passwords didn't match."
            if entered_email and not email:
                error_email = "That's not a valid email."
            self.write_form(entered_username,
                            '',
                            '',
                            entered_email,
                            error_username,
                            error_password,
                            error_verify,
                            error_email)
        else:
            self.redirect('/welcome?username='+entered_username)


class UserWelcome(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('username')
        self.response.out.write("Welcome, %s!"%name)


class Art(db.Model):
    title = db.StringProperty(required= True)
    art = db.TextProperty(required= True)
    date = db.DateTimeProperty(auto_now_add= True)


class Handler(webapp2.RedirectHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class ASCII_Page(Handler):
    def render_front(self, title ="", art = "", error = ""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY date DESC")
        self.render("front.html", title = title, art = art, error = error, arts = arts)

    def get(self, *args, **kwargs):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            a.put()
            self.redirect("/ascii")
        else:
            error = "We need both a title and some artwork"
            self.render_front(title, art, error)


class BlogFront(Handler):
    def get(self, *args, **kwargs):
        self.write("Here well be blog posts")

class NewPost(Handler):
    def get(self, *args, **kwargs):
        self.render("newpost.html")