class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score , high , idx = sum(nums) , sum(nums) , [0]

        for i,v in enumerate(nums,start = 1):
            if v == 0:
                score += 1
                
                if high < score:
                    idx = [i]
                    high = score
                elif high == score:
                    idx.append(i)
                    
            else:
                score -= 1

        return idx