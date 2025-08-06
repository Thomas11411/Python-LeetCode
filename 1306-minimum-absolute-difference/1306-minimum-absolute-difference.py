class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sort_arr = sorted(arr)
        min_dist = min([abs(sort_arr[i] - sort_arr[i+1]) for i in range(len(sort_arr)-1)])
        res = []
        for j in range(len(sort_arr)-1):
            if abs(sort_arr[j] - sort_arr[j+1]) == min_dist:
                res.append([sort_arr[j] , sort_arr[j+1]])
        return res