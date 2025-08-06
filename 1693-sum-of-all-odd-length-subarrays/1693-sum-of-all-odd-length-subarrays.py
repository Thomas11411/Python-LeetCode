class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = 0
        res = 0
        while l < len(arr):
            i = 0
            temp = sum(arr[:l+1])
            res += temp
            while i+l+1 < len(arr):
                temp += (arr[i+l+1] - arr[i])
                res += temp
                i += 1
            l += 2
    
        return res