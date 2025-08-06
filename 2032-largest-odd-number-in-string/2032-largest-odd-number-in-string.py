class Solution:
    def largestOddNumber(self, num: str) -> str:
        judge = False
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                judge = True
                break
        if not judge:
            return ""
        return num[:i+1]