#https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        d1 = {0:["a","a"],
              1:["a","e"],
              2:["e","i"],
              3:["i","o"],
              4:["o","u"],
              5:["u","u"]
             }
        val = 0
        count = 0
        res = 0
        for x in word:
            if x in d1[val]:
                count += 1
                if d1[val][1] == x:
                    val += 1
                if val >= 5: 
                    res = max(res,count)
                    val = 5
            else:
                if x == "a":
                    count = 1
                    val = 1
                else:
                    val = 0
                    count = 0


        return res