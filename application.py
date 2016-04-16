import cgi
import datetime
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import urlfetch

import os
import jinja2
import urllib, hashlib
import json


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__).split('/')[:-1])),
    extensions=['jinja2.ext.autoescape'],
    autoescape=False)

def setTemplate(self, template_values, templateFile):
    _templateFolder = 'views/'
    # add Defaults
    template_values['_templateFolder'] = _templateFolder
    template_values['_year'] = str(datetime.datetime.now().year)


    path = os.path.normpath(_templateFolder+templateFile)
    template = JINJA_ENVIRONMENT.get_template(path)
    self.response.write(template.render(template_values))


class Contact(webapp2.RequestHandler):
    def get(self, mailSent=False):
        data = {'mailSent':mailSent}
        setTemplate(self, data, 'contact.html')

    def post(self):
        email   = self.request.get('email')
        name    = self.request.get('name')
        message = self.request.get('message')

        sender_address = "Rowan Cockett<rowanc1@gmail.com>"
        email_to = "Rowan Cockett <rowanc1@gmail.com>"
        email_subject = "New Email from GeoSci.xyz"
        email_message = "Forwarded message:\n\nFrom: %s <%s>\n\n\n%s\n" % (name,email,message)

        mail.send_mail(sender_address, email_to, email_subject, email_message)
        self.get(mailSent=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        setTemplate(self, {"indexPage":True}, 'index.html')

class Who(webapp2.RequestHandler):
    def get(self):
        setTemplate(self, {"indexPage":False}, 'who.html')

class Why(webapp2.RequestHandler):
    def get(self):
        setTemplate(self, {"indexPage":False}, 'why.html')

class NotFoundPageHandler(webapp2.RequestHandler):
    def get(self):
        self.error(404)
        # self.redirect('404.html')
        setTemplate(self, {"indexPage":False}, '404.html')
        # self.response.out.write('404.html')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/why', Why),
    ('/who', Who),
    ('/contact', Contact),
    ('/.*', NotFoundPageHandler),
], debug=os.environ.get("SERVER_SOFTWARE", "").startswith("Dev"))