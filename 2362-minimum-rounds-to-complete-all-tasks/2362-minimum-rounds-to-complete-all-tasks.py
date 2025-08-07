class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter

        res = 0

        for i in Counter(tasks).values():
            if i % 3 == 2:
                res += (i - 2) // 3 + 1
            elif i > 1 and i % 3 == 1:
                res += (i - 4) // 3 + 2
            elif i % 3 == 0:
                res += i // 3
            else:
                return -1
        
        return res