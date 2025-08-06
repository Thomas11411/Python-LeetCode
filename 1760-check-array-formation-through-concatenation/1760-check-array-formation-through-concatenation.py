class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        all_dict = { i[0]: i for i in pieces }
        res = []
        for j in arr:
            res += all_dict.get(j , [])
        return arr == res