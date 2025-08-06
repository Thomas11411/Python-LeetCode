class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frog_dict = {i:0 for i in "croak"}
        res = 0
        for x in croakOfFrogs:
            frog_dict[x] += 1
            if not frog_dict["c"] >= frog_dict["r"] >= frog_dict["o"] >= frog_dict["a"] >= frog_dict["k"]:
                return -1
            res = max(res, frog_dict['c'] - frog_dict['k'])
            
        return res if len(set(frog_dict.values())) == 1 else -1
