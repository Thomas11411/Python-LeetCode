class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = [0] * 26
        s2_dict = [0] * 26

        for i in s1:
            s1_dict[ord(i) - ord('a')] += 1
            
        for i in range(len(s2)):
            s2_dict[ord(s2[i]) - ord('a')] += 1
    
            if i >= len(s1):
                s2_dict[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if s1_dict == s2_dict:
                return True
        return False