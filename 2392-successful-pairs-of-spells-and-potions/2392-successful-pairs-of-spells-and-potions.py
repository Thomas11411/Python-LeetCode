class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        length = len(potions)

        for i in spells:

            sd = success / i
            l = 0
            r = len(potions)

            while l < r:
                mid = l + (r - l) // 2
                if potions[mid] >= sd:
                    r = mid
                else:
                    l = mid + 1

            res.append(length - l)

        return res