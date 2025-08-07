class Solution:
    def minimumSum(self, num: int) -> int:
        new = sorted([i for i in str(num)])
        return (int(new[0]) + int(new[1])) * 10 + int(new[2]) + int(new[3])