class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s_num = str(num)
        res = 0

        for i in range(len(s_num) - k + 1):
            c = int(s_num[i:i + k])
            if c and num % c == 0:
                res += 1

        return res