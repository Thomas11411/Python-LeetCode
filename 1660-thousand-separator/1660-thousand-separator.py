class Solution:
    def thousandSeparator(self, n: int) -> str:
        str_n = str(n)
        res = []
        for i, v in zip(reversed(range(len(str_n)+1)), str_n):
            res.append(v)
            if i // 3 > 0 and i % 3 == 1:
                res.append(".")
        return ''.join(res)