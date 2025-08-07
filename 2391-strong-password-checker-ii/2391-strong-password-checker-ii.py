class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False
        
        check = [False] * 4

        for i in range(len(password)):

            if i > 0 and password[i - 1] == password[i]:
                return False

            if password[i].isupper():
                check[0] = True
            elif password[i].islower():
                check[1] = True
            elif password[i].isnumeric():
                check[2] = True
            else:
                check[3] = True

        return all(check)