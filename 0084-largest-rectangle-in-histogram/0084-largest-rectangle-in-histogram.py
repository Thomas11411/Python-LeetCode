class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i,v in enumerate(heights):
            while stack and stack[-1][1] > v:
                idx , h = stack.pop()
                w = (i - stack[-1][0] - 1)
                res = max(res,w * h)
            stack.append([i,v])

        return res  