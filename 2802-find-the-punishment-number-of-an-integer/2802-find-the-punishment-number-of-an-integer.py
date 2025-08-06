class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partition(s, target):
            if len(s) == 0 and target == 0: return True
            if target < 0: return False
            
            for i in range(len(s)):
                l = s[:i+1]
                r = s[i+1:]
                
                if partition(r, target - int(l)): return True
                
            return False

        res = 0

        for i in range(1, n + 1):
            n_str = str(i ** 2)
            
            if partition(n_str, i): res += (i ** 2)

        return res