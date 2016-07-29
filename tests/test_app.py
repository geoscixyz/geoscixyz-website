import os
import unittest
import sys
import webtest

sys.path.append('../geoscixyz')

from geoscixyz import *

from google.appengine.ext import testbed

class AppTest(unittest.TestCase):
    def setUp(self):
        # Create a WSGI application.
        # app = webapp2.WSGIApplication([('/', HelloWorldHandler)])
        # Wrap the app with WebTest’s TestApp.
        self.testapp = webtest.TestApp(app)

    # Test the handler.
    def testHelloWorldHandler(self):
        response = self.testapp.get('/')
        # response
        self.assertEqual(response.status_int, 200)
        # self.assertEqual(response.normal_body, 'Hello World!')
        # self.assertEqual(response.content_type, 'text/plain')

if __name__ == '__main__':
    unittest.main()
