class Solution:
    def maxProduct(self, n: int) -> int:
        new = sorted([int(i) for i in str(n)], reverse = True)
        return new[0] * new[1]