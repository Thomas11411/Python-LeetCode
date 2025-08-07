class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l , r , p_c = [] , [] , 0
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i == pivot:
                p_c += 1
            else:
                r.append(i)

        return l + ([pivot] * p_c) + r