# coding: utf-8

import unittest

class Solution(unittest.TestCase):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in xrange(l):
            for j in xrange(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def test_twoSum(self):
        expect = [0, 1]
        actual = self.twoSum([2,7,11,15], 9)
        assert expect == actual


if __name__ == '__main__':
    #unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(Solution)
    suite = unittest.TestSuite()
    suite.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Solution))
    unittest.TextTestRunner(verbosity=2).run(suite)



