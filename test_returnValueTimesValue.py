from unittest import TestCase
import unittest


class TestReturnValueTimesValue(unittest.TestCase):
    def test_returnValueTimesValue(self):
        TestCase = 2
        self.assertEqual(TestCase, 2, "You passed")


if __name__ == '__main__':
    unittest.main()
