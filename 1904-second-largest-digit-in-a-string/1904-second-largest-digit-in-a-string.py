class Solution:
    def secondHighest(self, s: str) -> int:
        first , second = -1 , -1
        for i in s:
            if i.isnumeric():
                if second < int(i) < first:
                    second = int(i)
                elif first < int(i):
                    second = first
                    first = int(i)
        return second