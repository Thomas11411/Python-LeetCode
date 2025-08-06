from collections import Counter
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dic = {i:v for i,v in Counter(s).items()}
        count = 0
        for i in s:
            dic[i] -= 1
            if dic['R'] == dic['L']:
                count += 1
        return count