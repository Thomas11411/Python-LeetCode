class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i, j, k = False, False, False
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                if t[0] == target[0]: i = True
                if t[1] == target[1]: j = True
                if t[2] == target[2]: k = True
        return i and j and k 