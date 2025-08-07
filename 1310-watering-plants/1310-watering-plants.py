class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 1
        curr = capacity
        for i,v in enumerate(plants):
            if not i:
                curr -= v
            else:
                if curr >= v:
                    curr -= v
                    res += 1

                else:
                    res += (i * 2 + 1)
                    curr = (capacity - v)

        return res