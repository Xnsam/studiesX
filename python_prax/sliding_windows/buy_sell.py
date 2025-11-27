


def max_profit(prices: list[int]) -> int:
    max_p = 0

    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]
            max_p = max(max_p, sell - buy)
    return max_p

def max_profit(prices: list[int]) -> int:
    l , r = 0, 0
    max_p = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p


tests = [
    ([10, 1, 5, 6, 7, 1], 6),
    ([10, 8, 7, 5, 2], 0)
]

for idx, t in enumerate(tests):
    res = max_profit(t[0])
    print(idx, " ", res == t[1])
