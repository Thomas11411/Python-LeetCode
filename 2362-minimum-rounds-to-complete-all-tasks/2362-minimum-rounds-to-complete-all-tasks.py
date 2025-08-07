class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter

        res = 0

        for i in Counter(tasks).values():
            if i % 3 == 2:
                res += (i - 2) // 3 + 1
            elif i % 3 == 1:
                if i == 1:
                    return -1
                res += (i - 4) // 3 + 2
            else:
                res += i // 3
        return res