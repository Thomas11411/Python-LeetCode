class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        arr_dict = {}
        for i in arr:
            if i - difference in arr_dict:
                arr_dict[i] = arr_dict[i - difference] + 1    
            else:
                arr_dict[i] = 1
        
        return max(arr_dict.values())