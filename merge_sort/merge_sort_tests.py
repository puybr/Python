import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_arr1(self):
        result = merge_sort([2, 8, 6, 9, 1, 13])
        self.assertEqual(result, [1, 2, 6, 8, 9, 13])

    def test_arr2(self):
        result = merge_sort([8, 44, 65, 6, 33, 7])
        self.assertEqual(result, [6, 7, 8, 33, 44, 65])
    
    def test_arr3(self):
        result = merge_sort([9, 6, 10, 8, 3, 7, 8])
        self.assertEqual(result, [3, 6, 7, 8, 8, 9, 10])
       
if __name__ == '__main__':
    unittest.main()