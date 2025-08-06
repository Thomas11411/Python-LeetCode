class Solution:
    def partitionString(self, s: str) -> List[str]:
        res = []
        tmp = ""
        seen = set()

        for i in s:
            tmp += i
            if tmp not in seen:
                res.append(tmp)
                seen.add(tmp)
                tmp = ""

        return res