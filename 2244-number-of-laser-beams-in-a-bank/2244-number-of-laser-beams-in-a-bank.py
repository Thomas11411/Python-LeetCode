class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        pre = 0
        for i in bank:
            now = i.count('1')
            if now > 0:
                res += ( pre * now )
                pre = now
        return res