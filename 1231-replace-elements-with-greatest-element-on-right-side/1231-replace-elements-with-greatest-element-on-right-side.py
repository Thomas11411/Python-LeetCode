class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(1,len(arr)):
            res.append(max(arr[i:]))
        res.append(-1)
        return res