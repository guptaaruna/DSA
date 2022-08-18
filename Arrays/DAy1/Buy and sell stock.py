def maxProfit(prices):
    max=prices[0]
    min=prices[0]
    dif=0
    for i in prices:
        if i < min:
            min=i
            max=i
        if i>max:
            max=i
        if dif<(max-min):
            dif=max-min
    return (dif)

prices=[7,1,5,3,6,4]
print(maxProfit(prices))