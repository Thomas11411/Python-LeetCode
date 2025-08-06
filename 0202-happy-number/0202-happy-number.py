class Solution:
    def isHappy(self, n: int) -> bool:
        p=[n]
        if n==1:
            return True
        while n>1:
            res=0
            x=str(n)
            for i in x:
                res+=int(i)**2
            if res in p:
                return False
            if res==1:
                return True
            p.append(res)
            n=res