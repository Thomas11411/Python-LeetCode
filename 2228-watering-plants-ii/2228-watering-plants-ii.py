class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        A_can = capacityA
        B_can = capacityB
        res = 0

        def f(nowcapacity,plants,capacity,refill):
            if nowcapacity < plants:
                refill += 1
                nowcapacity = capacity
            nowcapacity -= plants
            return refill,nowcapacity

        A_place = 0
        B_place = len(plants) - 1

        while A_place < B_place:

            res , A_can = f(A_can,plants[A_place],capacityA,res)
            A_place += 1

            res , B_can = f(B_can,plants[B_place],capacityB,res)
            B_place -= 1

        if A_place == B_place and plants[A_place] > max(A_can,B_can):
            res += 1
        return res