class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        i , res = 2 , []
        if finalSum % 2 == 0:
            while i <= finalSum:
                res.append(i)
                finalSum -= i
                i += 2
            res[-1] += finalSum

        return res