class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                #cnt = 0
                cnt = sum(i != j for i,j in zip(q,d))
                if cnt <= 2:
                    res.append(q)
                    break

        return res