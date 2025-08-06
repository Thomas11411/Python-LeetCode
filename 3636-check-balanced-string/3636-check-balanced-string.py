class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(int(num[i]) if i % 2 == 0 else -int(num[i]) for i in range(len(num))) == 0