class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        one , two = [],[]
        
        for i in nums:
            if i % 3 == 1:
                one.append(i)
            if i % 3 == 2:
                two.append(i)
        
        if sum(nums) % 3 == 1:
            if len(one) < 1 and len(two) < 2:
                return 0
            elif len(one) >= 1 and len(two) < 2:
                b = one[0]
            elif len(one) < 1 and len(two) >= 2:
                b = sum(two[0:2])
            else:
                b = min(one[0] , sum(two[0:2]))
        elif sum(nums) % 3 == 2:    
            if len(one) < 2 and len(two) < 1:
                return 0
            elif len(one) >= 2 and len(two) < 1:
                b = sum(one[0:2])
            elif len(one) < 2 and len(two) >= 1:
                b = two[0]
            else:
                b = min(sum(one[0:2]) , two[0])
        else:
            return sum(nums)
        return sum(nums) - b