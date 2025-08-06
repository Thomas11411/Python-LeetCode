class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(len(str(low)),len(str(high))+1):
            for j in range(i,10):
                res.append(int(''.join(map(str,list(range(j - i + 1, j + 1))))))
        return list(filter(lambda x : low <= x <= high ,res))