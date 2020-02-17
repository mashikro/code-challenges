# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Input: [7,1,5,3,6,4]
# Output: 5

# Input: [7,6,4,3,1]
# Output: 0

# buy low first and then you can sell high

def maximize_profit(prices):
    profit = 0
    if prices:
        
        smallest_num = prices[0]

        for num in range(len(prices)-1):
          
            if prices[num] < smallest_num:
                smallest_num = prices[num]
                if (prices[num+1]-smallest_num) > profit:
                    profit = prices[num+1]-smallest_num
            else:
                if (prices[num+1]-smallest_num) > profit:
                    profit = prices[num+1]-smallest_num
    return profit


print(maximize_profit2([7,1,5,3,6,4])) # 5
print(maximize_profit2([7,6,4,3,1])) # 0
print(maximize_profit2([]))# 0
print(maximize_profit2([2,4,1])) #2


# runtime: 1 for loop: O(n) 





