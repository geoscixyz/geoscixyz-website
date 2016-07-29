import cgi
import datetime
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
    _templateFolder = 'templates/'
    # add Defaults
    template_values['_templateFolder'] = _templateFolder
    template_values['_year'] = str(datetime.datetime.now().year)


    path = os.path.normpath(_templateFolder+templateFile)
    template = JINJA_ENVIRONMENT.get_template(path)
    self.response.write(template.render(template_values))



class MainPage(webapp2.RequestHandler):
    def get(self):

        setTemplate(self, {"indexPage":True}, 'index.html')


class Why(webapp2.RequestHandler):
    def get(self):
        setTemplate(self, {}, 'why.html')

class Who(webapp2.RequestHandler):
    def get(self):
        setTemplate(self, {}, 'who.html')


class Contact(webapp2.RequestHandler):
    def get(self, mailSent=False):
        data = {'mailSent':mailSent}
        setTemplate(self, data, 'contact.html')

    def post(self):
        email   = self.request.get('email')
        name    = self.request.get('name')
        message = self.request.get('message')

        sender_address = "GeoSci Mail <lindseyheagy@gmail.com>"
        email_to = "Lindsey Heagy <lindseyheagy@gmail.com>"
        email_subject = "GeoSci Mail"
        email_message = "New email from:\n\n%s<%s>\n\n\n%s\n" % (name,email,message)

        mail.send_mail(sender_address, email_to, email_subject, email_message)
        self.get(mailSent=True)


class Images(webapp2.RequestHandler):
    def get(self):
        self.redirect('http://www.geosci.xyz'+self.request.path)


class Error(webapp2.RequestHandler):
    def get(self):
        setTemplate(self, {}, 'error.html')



app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/journal', Thoughts),
    ('/why', Why),
    ('/who', Who),
    ('/img/.*', Images),
    ('/contact', Contact),
    ('/.*', Error),
], debug=os.environ.get("SERVER_SOFTWARE", "").startswith("Dev"))
