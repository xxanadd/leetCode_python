def solution(s: str) -> str:
    l = list(s)
    res = ''
    mid_res = []
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            mid_res.append(l[i])
            for j in range(min(i, len(l))):
                if l[i+j] == l[i-j-1]:
                    mid_res.append(l[i+j])
                else:
                    tmp = ''.join(mid_res)
                    mid_res = []
                    if tmp > res:
                        res = tmp
                    break
        elif 1 <= i <= len(s) - 1 and l[i-1] == l[i+1]:
            mid_res.append(l[i])
            for j in range(1, min(i, len(l)) + 1):
                if l[i+j] == l[i-j]:
                    mid_res.append(l[i+j])
                else:
                    tmp = ''.join(mid_res)
                    mid_res = []
                    if tmp > res:
                        res = tmp
                        break
    return res
print(solution("babad"))

"""
babad
"""