class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        now = 0
        for i in s.split(" "):
            if i.isnumeric():
                if int(i) > now:
                    now = int(i)
                else:
                    return False
        return True