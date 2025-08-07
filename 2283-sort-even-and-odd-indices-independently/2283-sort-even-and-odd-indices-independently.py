class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        import heapq
        e , o , k =  [] , [] , 0

        while k < len(nums):
            if k % 2 == 0:
                heapq.heappush(e , nums[k])
            else:
                heapq.heappush(o , -nums[k])
            k += 1

        res = [0] * len(nums)
        for i in range(len(nums)):
            if i % 2 == 0:
                res[i] = heapq.heappop(e)
            else:
                res[i] = -heapq.heappop(o)
        

        return res