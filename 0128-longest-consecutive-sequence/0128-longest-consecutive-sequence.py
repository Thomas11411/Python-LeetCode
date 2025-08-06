class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        ans = 0
        while nums:
            n = nums.pop()
            count = 1
            
            up = n+1
            while up in nums:
                nums.remove(up)
                count += 1
                up += 1
                
            down = n-1
            while down in nums:
                nums.remove(down)
                count += 1
                down -= 1
                
            ans = max(ans, count)
        return ans