class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_sum = [(i,sum(z)) for i,z in enumerate(mat)]
        return [j[0] for j in sorted(mat_sum,key = lambda x : x[1])][:k]