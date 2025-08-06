class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = 0
        n = len(customers)
        for i in range(n):
            satisfied += (customers[i] *(1 - grumpy[i]))
            
        max_sum = 0
        for end in range(X):
            max_sum += (customers[end] * grumpy[end])
        cur_sum = max_sum
        
        start = 0
        while end < n - 1:
            cur_sum -= (customers[start] * grumpy[start])
            start += 1
            end += 1
            cur_sum += (customers[end] * grumpy[end])
            if cur_sum > max_sum:
                max_sum = cur_sum
                
        return max_sum + satisfied