class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    res.append(prices[i]-prices[j])
                    break
                if j == len(prices) - 1:
                    res.append(prices[i])
        res.append(prices[-1])

        return res
                