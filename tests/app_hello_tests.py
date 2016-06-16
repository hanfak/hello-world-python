import unittest
from app.hello import Hello

class HellowTest(unittest.TestCase):

    def setUp(self):
		self.subject = Hello()

    def test_1_return_number(self):
        expected = "Hello Han"
        self.assertEqual(expected, self.subject.hello("Han"))
