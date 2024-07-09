#Can skip left pointer to right if you found a better buying date, otherwise just scan the list of prices
def slide_a_window(prices):
    l,r = 0, 1
    best_profit = 0
    while r < len(prices):
        if prices[r] > prices[l]:
            curr_profit = prices[r] - prices[l]
            best_profit = max(best_profit,curr_profit)
        else:
            l = r
        r += 1

    return best_profit

def main():
    prices = [7,1,5,3,6,4]
    prices2 = [7,6,4,3,1]
    print(slide_a_window(prices))
    print(slide_a_window(prices2))

main()