class Solution:
    def sumGame(self, num: str) -> bool:
        sum_ , count = 0 , 0
        mid = len(num) // 2
        for i,v in enumerate(num):
            if v == "?":
                count = (count - 1 if i < mid else count + 1)
            else:
                sum_ = (sum_ + int(v) if i < mid else sum_ - int(v))

        if count % 2 == 1:
            return True

        return not(sum_ == count // 2 * 9)