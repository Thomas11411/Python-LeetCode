class Solution:
    def reformatNumber(self, number: str) -> str:

        temp = number.replace(' ','').replace('-','')


        res = []
        l = 0
        while l < len(temp):

            if len(temp) - l == 2:
                res += temp[l:l+2]
                return ''.join(res)
            elif len(temp) - l == 3:
                res += temp[l:l+3]
                return ''.join(res)
            elif len(temp) - l == 4:
                res += temp[l:l+2]
                res += "-"
                res += temp[l+2:l+4]
                
                return ''.join(res)
            
            res += temp[l:l+3]
            res += "-"
            l += 3