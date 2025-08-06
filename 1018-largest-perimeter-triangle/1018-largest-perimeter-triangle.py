class Solution:
    def isTri(self, a, b, c):
        if a < (b+c) and b < (a+c) and c < (a+b):
            return True
        return False
    
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A,reverse=True)
        for i in range(len(A)-2):
            if self.isTri(A[i], A[i+1], A[i+2]):
                return A[i]+A[i+1]+A[i+2]
        return 0