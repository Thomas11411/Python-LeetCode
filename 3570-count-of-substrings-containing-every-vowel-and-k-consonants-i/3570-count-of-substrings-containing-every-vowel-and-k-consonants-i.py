class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        from collections import defaultdict
        n = len(word)
        i = 0
        d = defaultdict(int)
        d["a"] = d["e"] = d["i"] = d["o"] = d["u"] = 0
        ccnt = 0
        res = 0

        for j in range(n):
            
            if word[j] in "aeiou": d[word[j]] += 1 
            else: ccnt += 1
            
            while ccnt > k and i < j:

                if word[i] in "aeiou": 
                    d[word[i]] -= 1 
                else: 
                    ccnt -= 1
                i += 1

            if all(d[v] > 0 for v in "aeiou") and ccnt == k:
                res += 1
                ii = i
                dd = d.copy()
                ccnt2 = ccnt
                while all(dd[v] > 0 for v in "aeiou") and ccnt2 == k and ii < j:
                    
                    if word[ii] in "aeiou": 
                        dd[word[ii]] -= 1 
                    else: 
                        ccnt2 -= 1
                    
                    if all(dd[v] > 0 for v in "aeiou") and ccnt2 == k: 
                        res += 1
                        
                    ii += 1

        return res