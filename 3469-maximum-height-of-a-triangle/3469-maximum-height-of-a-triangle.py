class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
                
        def check(b1, b2):
            res = 0
            while True:
                if res % 2 == 0:
                    b1 -= (res + 1)
                else:
                    b2 -= (res + 1)
                    
                if b1 < 0 or b2 < 0: return res
                
                res += 1
            
        return max(check(red, blue), check(blue, red))