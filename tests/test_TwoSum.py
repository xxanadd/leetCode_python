import unittest
from TwoSum import TwoSum


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        test = TwoSum()

        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]

        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                result = test.twoSum(nums, target)
                self.assertListEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
