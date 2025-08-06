class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        one , two = 'a' , 'b'
        if x < y:
            x , y , one , two = y , x , two , one


        one_count , two_count = 0 , 0

        res = 0
        for c in s:
            if c == one:
                one_count += 1
            elif c == two:
                if one_count > 0:
                    one_count -= 1
                    res += x
                else:
                    two_count += 1

            else:
                res += (y * min(one_count,two_count))
                one_count = 0
                two_count = 0

        res += (y * min(one_count,two_count))

        return res