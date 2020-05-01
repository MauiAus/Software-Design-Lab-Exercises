#Made By Marielle Gabriel

import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = 10 + 6
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()