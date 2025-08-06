class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        d = defaultdict(int)
        for l,r,c in segments:
            d[l] += c
            d[r] -= c
            
        left , color , res = None , 0 , []

        for right in sorted(d):
            if left is not None and color != 0:
                res.append((left,right,color))

            color += d[right]
            left = right
            
        return res