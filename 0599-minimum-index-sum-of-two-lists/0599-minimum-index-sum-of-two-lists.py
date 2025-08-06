class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mn = float("inf")
        for i,v in enumerate(list1):
            if v in list2:
                i2 = list2.index(v) + i
                if i2 < mn:
                    mn = i2
                    res = [v]
                elif i2 == mn:
                    res.append(v)
        return res