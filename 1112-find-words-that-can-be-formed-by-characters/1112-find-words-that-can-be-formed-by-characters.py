from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {i:v for i,v in Counter(chars).items()}
        res = 0
        for x in words:
            x_dic = {i:v for i,v in Counter(x).items()}
            res += len(x)
            for y in x:
                if y not in dic or dic[y] < x_dic[y]:
                    res -= len(x)
                    break
        return res