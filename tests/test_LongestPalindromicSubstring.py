import unittest
from LongestPalindromicSubstring import Solution


class LongestPalindromicSubstring(unittest.TestCase):
    def test_palindromic(self):
        test = Solution()

        test_cases = [
            ('babad', 'bab'),
            ('cbbd', 'bb'),
        ]

        for s, expected in test_cases:
            with self.subTest(string=s):
                result = test.longestPalindrome(s)
                self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
