from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_count = [[k,n] for k, n in Counter(arr).items()]
        return max([x[0] for x in arr_count if x[0] == x[1]]) if len([x[0] for x in arr_count if x[0] == x[1]]) else -1