class Solution:
    def reformat(self, s: str) -> str:
        letter = []
        num = []
        res = []

        for i in s:
            if i.isalpha():
                letter.append(i)
            else:
                num.append(i)
                
        if 0 <= len(letter) - len(num) <= 1:
            n = min(len(letter) , len(num))
            list1 = letter
            list2 = num
        elif len(num) - len(letter) == 1:
            n = min(len(letter) , len(num))
            list1 = num
            list2 = letter
        else:
            return ""
         
        for i in range(n):
            res.append(list1.pop())
            res.append(list2.pop())
            
        if list1:
            res.append(list1.pop())
            
        return "".join(res)