class Solution:
    def minimumBuckets(self, street: str) -> int:
        res = 0
        street = list(street)
        for i in range(len(street)):
            if street[i] == "H":
                if i > 0 and street[i - 1] == "B":
                    continue
                if i < len(street) - 1 and street[i + 1] == ".":
                    street[i + 1] = "B"
                    res += 1
                    continue
                if i > 0 and street[i - 1] == ".":
                    street[i - 1] = "B"
                    res += 1
                    continue
                return -1
        return res
