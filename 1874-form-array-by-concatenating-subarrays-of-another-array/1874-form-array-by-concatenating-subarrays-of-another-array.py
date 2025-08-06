class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        now = 0
        for i in groups:
            for j in range(now,len(nums)-len(i)+1):
                if nums[j:j+len(i)] == i:
                    now = j + len(i)
                    break
            else:
                return False
        return True 