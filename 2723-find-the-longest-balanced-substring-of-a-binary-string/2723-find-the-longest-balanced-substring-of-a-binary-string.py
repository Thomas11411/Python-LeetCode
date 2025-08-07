class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        sample = ''

        for i in range(25):
            
            sample = '0' + sample + '1'
            if sample not in s: return 2 * i
            
        return 50