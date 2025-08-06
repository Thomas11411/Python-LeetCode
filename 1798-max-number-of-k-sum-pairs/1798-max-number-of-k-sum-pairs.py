class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dict = dict()
        res = 0
        for i in nums:
            if k > i:
                if i in num_dict and num_dict[i] > 0:
                    num_dict[i] -= 1
                    res += 1
                else:
                    try:
                        num_dict[k - i] += 1
                    except:
                        num_dict[k - i] = 1
        return res