class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(map(lambda x: int(''.join([max(str(x))] * len(str(x)))), nums))
        