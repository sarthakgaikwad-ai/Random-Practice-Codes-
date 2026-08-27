#Q5
def min_coins(coins, amount):
    # dp[i] = minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


# Accept coin denominations from the user
coins_input = input("Enter coin denominations separated by space: ")
coins = list(map(int, coins_input.split()))

# Accept the target amount
amount = int(input("Enter the target amount: "))

result = min_coins(coins, amount)

if result == -1:
    print("It is not possible to make this amount with the given coins.")
else:
    print("Minimum number of coins required:", result)


#Q8
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    max_length = 0  
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
            else:
                dp[i][j] = 0  
    
    return max_length

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = longest_common_substring(string1, string2)
print("Length of the longest common substring:", result)

