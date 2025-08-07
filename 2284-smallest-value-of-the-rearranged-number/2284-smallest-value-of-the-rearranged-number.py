class Solution:
    def smallestNumber(self, num: int) -> int:
        
        s = sorted(str(abs(num)))
        
        if num <= 0:
            return -int(''.join(s[::-1]))

        idx = next(i for i,v in enumerate(s) if v > '0')
        s[idx] , s[0] = s[0] , s[idx]
        return int(''.join(s))
        