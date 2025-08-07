class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)

        odd , even = [] ,[]

        for i in num:
            if int(i) % 2:
                odd.append(i)
            else:
                even.append(i)

        even.sort() 
        odd.sort() 

        return int(''.join([odd.pop() if int(i) % 2 else even.pop() for i in num]))