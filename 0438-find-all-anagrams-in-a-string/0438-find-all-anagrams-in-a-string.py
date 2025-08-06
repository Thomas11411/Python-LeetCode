class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = [0] * 26
        s_dict = [0] * 26
        res = []
        
        for i in p:
            p_dict[ord(i) - ord("a")] += 1
        
        
        for i in range(len(s)):
            s_dict[ord(s[i]) - ord("a")] += 1
                
            if i >= len(p):
                s_dict[ord(s[i-len(p)]) - ord("a")] -= 1
            if s_dict == p_dict:
                res.append(i-len(p)+1)
                
        return res