class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - int((purchaseAmount + 5) // 10) * 10