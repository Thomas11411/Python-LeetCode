class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        x = -1
        x_list = []
        c = max([len(y) for y in nums])
        r = len(nums)
        res = []

        for i in range(c+r-1):
            if x < (r-1):
                x += 1
                x_list.append(x)
            for j in reversed(x_list):
                if nums[j]:
                    res.append(nums[j].pop(0))
                    if not nums[j]:
                        x_list.remove(j)

        return res