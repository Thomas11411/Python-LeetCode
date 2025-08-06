from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        deq = deque()
        window_product, count = 1, 0
        for i in nums:
            deq.append(i)
            window_product *= i
            while window_product >= k and deq:
                window_product /= deq.popleft()
            count += len(deq)
        return count