class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num2 > num1:
            num1 , num2 = num2 , num1

        res = 0

        while num2 > 0:
            res += (num1 // num2)
            num1 , num2 = num2 , num1 % num2

        return res