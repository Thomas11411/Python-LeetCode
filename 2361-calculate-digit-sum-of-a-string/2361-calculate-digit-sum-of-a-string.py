class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        temp  = ""
        for i in range(0,len(s),k):
            temp += str(sum(int(j) for j in s[i:i+k]))
        return self.digitSum(temp,k)
    