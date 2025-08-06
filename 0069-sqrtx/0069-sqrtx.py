class Solution:
    def mySqrt(self, x: int) -> int:
        self.x = x
        self.final = []
        self.final = math.floor(math.sqrt(x))
        return self.final