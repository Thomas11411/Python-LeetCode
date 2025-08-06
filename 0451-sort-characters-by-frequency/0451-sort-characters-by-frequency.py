from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count_s = Counter(s).items()
        sort_count_s = sorted(count_s, key = lambda x: x[1],reverse = True)
        final = []
        for i,v in sort_count_s:
            temp_list = [i] * v
            final += temp_list
        return ''.join(final)