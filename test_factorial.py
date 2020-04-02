import unittest
from factorial import factorial

class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)


if __name__ == "__main__":
    unittest.main(exit=False)