class Solution:
    def maximum69Number (self, num: int) -> int:
        list_num = list(str(num))
        res = [num]
        for i in range(len(list_num)):
            list_num2 = list_num.copy()
            if list_num[i] == '6':
                list_num2[i] = '9'
            else:
                list_num2[i] = '6'
            res.append(int(''.join(list_num2)))
        
        return max(res)
        