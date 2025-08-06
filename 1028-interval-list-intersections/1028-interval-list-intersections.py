class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        A_ind , B_ind = 0 , 0
        res = []
        while A_ind < len(A) and B_ind <len(B):
            A_start , A_end = A[A_ind]
            B_start , B_end = B[B_ind]
            G_start , G_end = max(A_start,B_start) , min(A_end,B_end)
            
            if G_start <= G_end:
                res.append([G_start , G_end])
            
            if A_end < B_end:
                A_ind += 1
            else:
                B_ind += 1
        
        return res