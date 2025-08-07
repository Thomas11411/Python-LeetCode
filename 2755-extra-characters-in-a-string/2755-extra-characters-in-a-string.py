class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        @cache

        def dp(i, extra):
            if i >= len(s):
                return extra
            
            min_extra = dp(i + 1, extra)
            
            for w in dictionary:
                if s[i:].startswith(w):
                    min_extra = min(
                        min_extra,
                        dp(i + len(w), extra - len(w))
                    )
                    
            return min_extra

        return dp(0, len(s))