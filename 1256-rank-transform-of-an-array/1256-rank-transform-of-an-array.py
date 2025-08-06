class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {j:i+1 for i, j in enumerate(sorted(set(arr)))}
        return [dic[x] for x in arr]