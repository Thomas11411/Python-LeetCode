class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:

        cur = nums[0]
        res = [0]
        for i in nums:
            if i > cur:
                cur = i
            res.append(res[-1] + i + cur)
            
        return res[1::]