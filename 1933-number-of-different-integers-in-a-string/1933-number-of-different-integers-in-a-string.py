class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num = [str(i) for i in range(0,10)]
        res , temp = [] , []
        for i in word:
            if i in num:
                temp.append(i)
            elif i not in num and temp:
                res.append(int(''.join(temp)))
                temp = []
        if temp:
            res.append(int(''.join(temp)))
        return len(set(res))