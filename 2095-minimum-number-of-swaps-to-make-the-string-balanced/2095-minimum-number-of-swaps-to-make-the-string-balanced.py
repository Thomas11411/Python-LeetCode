class Solution:
    def minSwaps(self, s: str) -> int:
        count , ans = 0 , 0
        for i in s:
            if i == "]":
                if count == 0:
                    count += 1
                    ans += 1
                else:
                    count -= 1
            else:
                count += 1
        return ans