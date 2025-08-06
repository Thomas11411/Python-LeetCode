class Solution:
    def maxLength(self, arr: List[str]) -> int:
        count = 0
        arr_list = ['']
        for i in arr:
            for j in arr_list:
                if len(i + j) == len(set(i + j)):
                    count = max(count,len(i + j))
                    arr_list.append(i + j)
        return count