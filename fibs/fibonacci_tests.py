import unittest
from fibonacci import output

class TestFibonacciSequence(unittest.TestCase):

    def test_fib1(self):
        result = output(1)
        self.assertEqual(result, [0, 1])

    def test_fib8(self):
        result = output(8)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_fib15(self):
        result = output(15)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])

    def test_fib19(self):
        result = output(19)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])
        

if __name__ == '__main__':
    unittest.main()