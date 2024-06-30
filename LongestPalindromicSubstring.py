class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = list(s)
        if len(l) > 0:
            res = l[0]
        else:
            return ''
        tmp_res = []
        for i in range(1, len(l)):
            # Если четное количество в последовательности
            if l[i] == l[i - 1]:
                tmp_res.append(l[i])
                tmp_res.insert(0, l[i])
                for j in range(1, min(i, len(l) - i)):
                    left = l[i + j]
                    right = l[i - j - 1]
                    if l[i + j] == l[i - j - 1]:
                        tmp_res.append(left)
                        tmp_res.insert(0, right)
                    else:
                        break
                if len(tmp_res) > len(res):
                    res = ''.join(tmp_res)
                tmp_res = []
            # Если нечетное количество символов в последовательности
            if 1 <= i <= len(l) - 2 and l[i - 1] == l[i + 1]:
                tmp_res.append(l[i])
                for j in range(1, min(i + 1, len(l) - i)):
                    left = l[i + j]
                    right = l[i - j]
                    if left == right:
                        tmp_res.insert(0, left)
                        tmp_res.append(right)
                    else:
                        break
                if len(tmp_res) > len(res):
                    res = ''.join(tmp_res)
                tmp_res = []
        return res