import unittest
from app.hello import Hello

class HelloTest(unittest.TestCase):

    def setUp(self):
		self.subject = Hello()

    def test_1_return_greeting(self):
        """name appended to hello"""
        expected = "Hello Han"
        self.assertEqual(expected, self.subject.hello("Han"))
