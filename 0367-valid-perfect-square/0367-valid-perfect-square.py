class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        
        for i in range(int(num / 2)+1):
            if i ** 2 == num:
                return True
            elif i ** 2 > num:
                return False