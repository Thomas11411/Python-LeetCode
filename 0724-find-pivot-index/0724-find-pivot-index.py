class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        currentSum = 0
        
        for i, e in enumerate(nums):
            currentSum += e           
            if currentSum == totalsum:
                return i      
            totalsum -= e
        return -1