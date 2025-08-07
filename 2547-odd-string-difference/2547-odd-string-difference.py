class Solution:
    def oddString(self, words: List[str]) -> str:
        from collections import defaultdict

        d = defaultdict(list)

        for i,v in enumerate(words):
            d[tuple(ord(v[j]) - ord(v[j - 1]) for j in range(1,len(v)))].append(i)
            
        return words[[i[0] for i in d.values() if len(i) == 1][0]]