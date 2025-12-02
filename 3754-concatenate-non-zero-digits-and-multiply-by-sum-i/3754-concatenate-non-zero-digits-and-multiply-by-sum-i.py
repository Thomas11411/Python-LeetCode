class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = sum(int(i) for i in str(n) if i != "0")
        n2 = str(n).replace("0", "")
        if n2 == "": return 0
        return int(n2) * total