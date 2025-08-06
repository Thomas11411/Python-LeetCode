class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        nowBottles = numBottles
        countBottles = numBottles
        while nowBottles >= numExchange:
            countBottles += nowBottles // numExchange
            nowBottles = nowBottles // numExchange + nowBottles % numExchange
        return countBottles