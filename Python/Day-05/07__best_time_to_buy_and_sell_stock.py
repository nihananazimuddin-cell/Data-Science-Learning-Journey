#================================================================
# Day 05 - Best Time to Buy and Sell Stock (Brute Force)
# Date: 03 August 2026
#
# Problem:
# Given the daily stock prices, determine the maximum profit
# that can be earned by buying the stock once and selling it
# once in the future. If no profit can be made, return 0.
#
# Concepts Learned:
# • Brute-force approach using nested loops
# • Comparing every possible buy-sell combination
# • Tracking the maximum profit
# • Index-based traversal of lists
# • Edge case handling (single element, no profit, equal prices)
# • Time Complexity: O(n²)
# • Space Complexity: O(1)
#
# Skills Practiced:
# • Problem decomposition
# • Algorithm design
# • Loop control (for + while)
# • Variable naming for readability
# • Debugging logical errors
# • Optimizing code readability
#================================================================

stock_prices = list(map(int, input("Enter the daily stock prices : ").split()))

def decide_buy_sell_stocks(stock_prices):
    num_of_days =len(stock_prices)
    best_profit = 0

    for buy_day in range(num_of_days-1):
        sell_day = buy_day + 1

        profit = 0    
        while sell_day < num_of_days:
            new_profit = stock_prices[sell_day] - stock_prices[buy_day] 
            if new_profit > profit :
                profit = new_profit
            sell_day += 1

        if profit > best_profit:
            best_profit = profit
            
    return best_profit       
            
result = decide_buy_sell_stocks(stock_prices)
print(f"Best profit = {result}")
