class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        tmp = set()

        for i in s:
            if i in tmp:
                res += 1
                tmp = set()
            tmp.add(i)

        return res