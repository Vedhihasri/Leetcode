class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        b=math.floor((purchaseAmount + 5) / 10) * 10
        return 100-b