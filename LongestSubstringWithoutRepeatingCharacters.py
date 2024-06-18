# def lengthOfLongestSubstring(s: str) -> int:
#     ts = tuple(s)
#     max_substring = ''
#     if len(ts) > 0:
#         max_substring = ts[0]
#     array = [[0 for _ in range(len(s))] for _ in range(len(s))]
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             if i == j:
#                 array[i][j] = ts[i]
#             else:
#                 if ts[j] not in array[i][j - 1]:
#                     substring = array[i][j - 1] + ts[j]
#                     array[i][j] = substring
#                     if len(substring) > len(max_substring):
#                         max_substring = substring
#                 else:
#                     break
#     return len(max_substring)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ts = tuple(s)
        max_substring = ''
        if len(ts) > 0:
            max_substring = ts[0]
        substring = []
        for i in range(len(ts)):
            if ts[i] not in substring:
                substring.append(ts[i])
                if len(substring) > len(max_substring):
                    max_substring = ''.join(substring)
            else:
                position = substring.index(ts[i])
                substring = substring[position + 1:]
                substring.append(ts[i])
        return len(max_substring)
