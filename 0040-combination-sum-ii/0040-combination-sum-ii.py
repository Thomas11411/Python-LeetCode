class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        fin = []
        def comb(c,t,r):
            if t == 0:
                fin.append(r)

            else:
                for i in range(len(c)):
                    if i > 0 and c[i] == c[i-1]:
                        continue
                    if c[i] <= t:
                        comb(c[i+1:],t - c[i],r + [c[i]])
        comb(candidates,target,[])

        return fin