def minimumWaitingTime(queries):
    total_waiting_time = 0
    for idx, duration in enumerate(sorted(queries)):
        queriesLeft = len(queries) - (idx + 1)
        total_waiting_time += duration * queriesLeft
        print(total_waiting_time, duration, queriesLeft)

    return total_waiting_time


print(minimumWaitingTime([1, 2, 2, 3, 6]))


def maxProfit(prices):
    if not prices:
        return 0
    min_price, highest_profit = float('inf'), 0
    for price in prices:
        if price < min_price: min_price = price
        if price - min_price > highest_profit:
            highest_profit = price - min_price
    return highest_profit
