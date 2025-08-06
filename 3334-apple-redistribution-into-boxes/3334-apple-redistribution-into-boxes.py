class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        sum_ = sum(apple)
        capacity.sort(reverse = True)

        for i in range(0, len(capacity)):
            sum_ -= capacity[i]
            if sum_ <= 0:
                return i + 1


        