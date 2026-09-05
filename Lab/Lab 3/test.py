def coin_change(coins, amount):
    # dp[i] = minimum number of coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    
    # 0 coins are needed to make amount 0
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter the amount: "))

# Output
result = coin_change(coins, amount)

if result == -1:
    print("Amount cannot be formed using the given coins.")
else:
    print("Minimum number of coins required:", result)