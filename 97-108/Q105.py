# 105.	**Coin Change (Greedy)**

# •	Given a list of coin denominations and a target amount, find the minimum number of coins needed using a greedy approach.

def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        count += amount // coin
        amount %= coin
    
    return count if amount == 0 else -1

coins = [1, 2, 5]
amount = 11

print(coin_change(coins, amount))  # Output: 3
# The minimum number of coins needed is 3 (5, 5, 1) to make 11.