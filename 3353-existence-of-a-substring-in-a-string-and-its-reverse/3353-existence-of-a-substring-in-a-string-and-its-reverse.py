class Solution:
    def isSubstringPresent(self, s: str) -> bool:
                
        for i in range(1, len(s)):
            if s[(i-1):(i+1)] in s[::-1]: return True

        return False