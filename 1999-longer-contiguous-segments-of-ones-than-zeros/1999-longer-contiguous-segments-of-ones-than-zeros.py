class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if len(s) == 1:
            if s[0] == "1":
                return True
            else:
                return False


        count0 , count1 , res0 , res1 = 0 , 0 , 0 , 0 
        if s[0] == "0":
            count0 += 1
        else:
            count1 += 1


        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                if s[i] == "1":
                    count1 += 1
                else:
                    count0 += 1
            else:
                if s[i] == "1":
                    count1 = 1
                else:
                    count0 = 1

            res1 = max(res1,count1)
            res0 = max(res0,count0)

        return res1 > res0
