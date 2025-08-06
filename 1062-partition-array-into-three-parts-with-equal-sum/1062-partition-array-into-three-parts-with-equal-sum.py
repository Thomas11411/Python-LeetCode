class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        target = sum(A) // 3
                
        count = 0
        currSum = 0
        for a in A:
            currSum += a
            if currSum == target:
                if count == 2:
                    return True
                count += 1
                currSum = 0
        
        return False
            