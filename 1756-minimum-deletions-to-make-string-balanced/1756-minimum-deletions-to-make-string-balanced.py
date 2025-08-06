class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        right_b_count = [0] * (n + 1)
        left_a_count = [0] * (n + 1)
        b_count = 0
        a_count = 0


        for i in range(n):
            if s[i] == "a":
                a_count += 1
            else:
                b_count += 1

            if i == 0:
                if s[i] == "a":
                    left_a_count[i + 1] = 1
                else:
                    right_b_count[i + 1] = 1
            else:
                left_a_count[i + 1] = a_count
                right_b_count[i + 1] = b_count
                
        res = float("inf")

        for i in range(n):
            a_delete = left_a_count[-1] - left_a_count[i + 1]
            b_delete = right_b_count[i]
            res = min(res,a_delete+b_delete)

        return res