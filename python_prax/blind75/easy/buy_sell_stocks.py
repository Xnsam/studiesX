

def buy_sell(prices: list) -> int:
    l, r = 0, 0
    max_p = 0

    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1

    return max_p


tests = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0)
]


for idx, t in enumerate(tests):
    res = buy_sell(t[0])
    print(idx, " ", "Test passed" if res == t[1] else "Test Failed")