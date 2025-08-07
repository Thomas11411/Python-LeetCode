class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return len(str(num)) == 1 or str(num)[-1] != '0'