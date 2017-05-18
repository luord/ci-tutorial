import unittest

from app import app


class Test(unittest.TestCase):
    def test(self):
        result = app.test_client().get('/')

        self.assertEqual(result.data.decode('UTF-8'), 'Hello World!')
