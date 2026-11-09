import unittest
import sys
import os

# Add parent directory to path so app can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import add_numbers, subtract_numbers

class TestCalculatorApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 999) #failing test case
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(0, 4), -4)

if __name__ == "__main__":
    unittest.main()