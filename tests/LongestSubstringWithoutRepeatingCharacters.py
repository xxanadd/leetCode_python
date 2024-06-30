import unittest
from LongestSubstringWithoutRepeatingCharacters import Solution


class LongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_two_sum(self):
        test = Solution()

        test_cases = [
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
        ]

        for s, expected in test_cases:
            with self.subTest(string=s):
                result = test.lengthOfLongestSubstring(s)
                self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
