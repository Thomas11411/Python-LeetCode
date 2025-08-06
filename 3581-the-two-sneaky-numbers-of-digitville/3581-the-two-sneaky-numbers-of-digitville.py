class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
                
        from collections import Counter

        d = Counter(nums)
        return [i for i,v in d.items() if v == 2]