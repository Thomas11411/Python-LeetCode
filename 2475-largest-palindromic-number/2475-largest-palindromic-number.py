class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter

        if num == ("0" * len(num)):
            return "0" 


        d = Counter(num)

        head = ""
        mid = ""


        for i in "9876543210":
            cur = d[i]
            if d[i] % 2 and mid == "":
                mid = i
            head += i * (cur // 2)
            
        if head != "" and head[0] == "0":
            head = ""

        return head + mid + head[::-1]