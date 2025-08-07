class Solution:
    def minimumPartition(self, s: str, k: int) -> int:

        res = 1
        cur = 0
        for i in s:
            if int(i) > k:
                return -1
                
            cur = cur * 10 + int(i)
            
            if cur > k:
                res += 1
                cur = int(i)

        return res