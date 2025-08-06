class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            for j in range(1,len(temp)):
                if temp[j - 1] >= temp[j]:
                    break
            else:
                return True
        return False
