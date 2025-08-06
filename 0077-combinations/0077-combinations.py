import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_num = list(range(1,n+1))
        x = list(itertools.combinations(all_num,k))
        return x