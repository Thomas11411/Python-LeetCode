class Solution(object):
    def sortArrayByParity(self,x):
        self.x = x
        self.final = []
        odd = []
        even = []

        for i in range(0,len(x)):
            if x[i] % 2 == 0:
                even.append(x[i])
            else:
                odd.append(x[i])
        self.final = even + odd
        return self.final
        
        