class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        dic = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for ch in text:
            if ch in dic:
                dic[ch] += 1
        dic["l"] = dic["l"] // 2
        dic["o"] = dic["o"] // 2
        return min(dic.values())