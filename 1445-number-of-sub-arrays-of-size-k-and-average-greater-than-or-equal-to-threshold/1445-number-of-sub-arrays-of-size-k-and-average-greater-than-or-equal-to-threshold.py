class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        count = int(total >= k * threshold)
        
        for i in range(k, len(arr)):
            total += arr[i] - arr[i-k]
            if total >= k * threshold:
                count += 1
        
        return count