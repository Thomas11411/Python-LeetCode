class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = str(x)

        mid = (len(new_x) // 2) 

        return new_x[:mid] == new_x[::-1][:mid]