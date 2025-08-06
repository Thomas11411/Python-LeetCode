class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start , nowcost , res = 0 , 0 , 0
        for end in range(len(s)):
            nowcost += abs(ord(s[end]) - ord(t[end]))
            if nowcost <= maxCost:
                res = max(res ,end - start + 1)

            else:
                while nowcost > maxCost:
                    nowcost -= abs(ord(s[start]) - ord(t[start]))
                    start += 1
        return res