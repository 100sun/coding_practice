from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, highest_profit = float("inf"), 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > highest_profit:
                highest_profit = price - min_price
        return highest_profit
