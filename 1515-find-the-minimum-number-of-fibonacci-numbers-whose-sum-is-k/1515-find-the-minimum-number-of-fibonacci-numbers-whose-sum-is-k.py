class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        Fib_seq = [1,1]
        x = 0
        while x < k:
            x = Fib_seq[-1] + Fib_seq[-2]
            if x <= k:
                Fib_seq.append(x)

        count = 0
        for i in range(len(Fib_seq)-1,-1,-1):
            if Fib_seq[i] <= k:
                k -= Fib_seq[i]
                count += 1
            if k == 0:
                return count

        