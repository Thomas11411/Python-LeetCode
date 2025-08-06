class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            while stack and len(nums) - i - k + len(stack) > 0 and nums[i] < stack[-1]:
                stack.pop()
            stack.append(nums[i])
        return stack[:k]