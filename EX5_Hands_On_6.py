import unittest

def double(x):
    return x * 2

class TestCalc(unittest.TestCase):
    def testdouble(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(4), 4)
        self.assertEqual(double(0), 0)
        self.assertEqual(double(-2), 4)

if __name__ == '__main__':
    unittest.main()