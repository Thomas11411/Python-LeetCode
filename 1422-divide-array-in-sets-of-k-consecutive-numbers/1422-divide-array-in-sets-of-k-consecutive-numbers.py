from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums)%k != 0:
            return False
        
        if k == 1:
            return True

        nums.sort()
        nums_dict = Counter( nums )

        for n in nums:         
            now_count = nums_dict[n]
            if now_count == 0:
                continue
                
            for i in range(k):
                if nums_dict[n+i] < now_count:
                    return False                
                nums_dict[n+i] -= now_count
                
        return True