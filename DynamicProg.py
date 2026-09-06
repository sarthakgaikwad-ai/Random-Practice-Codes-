memo ={}         #create an empty dic for storing as this is memorization(storage)(top down)
def fib(n):      
    if n<=1:
        return n    #base case 
    
    if n in memo:    
        return memo[n]      #if you have already calculated answer for n then return it again instead of calculating it 
    
    memo[n]= fib(n-1)+fib(n-2)      
    return memo[n]          #if you have not already calculated answer for n then calculate and return the answer 
print(fib(6))       #display the output (8)


#Tabulation
def fib(n):
    if n <= 1:
        return n        #base case 

    dp = [0, 1]  #initial case 

    for i in range(2, n + 1):   
        dp.append(dp[i-1] + dp[i-2]) #same as fib(n-1)+fib(n-2) but .append to add in list as it is tabulation 

    return dp[n]
print(fib(8))           #output 21


#Longest Common Subsequence (finding length )
def lcs(X, Y):

    m = len(X)
    n = len(Y)           #

    dp = [[0] * (n + 1) for _ in range(m + 1)]      #creating dp table

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:            #case 1 if X=Y(macthing charecters)
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:                               #case 2 if X not equal to Y(non macthing charecters )
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


print(lcs("ABCDFGHWQY", "ACDEEGTH"))         #output 5

#knapsack
def knapsack(wt, val, W):

    n = len(wt)

    dp = [[0] * (W + 1) for _ in range(n + 1)]      #creating dp table

    for i in range(1, n + 1):

        for w in range(W + 1):

            if wt[i-1] <= w:        #take it condition 

                dp[i][w] = max(
                    dp[i-1][w],
                    dp[i-1][w-wt[i-1]] + val[i-1]
                )

            else:

                dp[i][w] = dp[i-1][w]           #don't take it condition 

    return dp[n][W]


print(knapsack(
    [2, 3, 4, 1],
    [3, 4, 5, 1],
    5
))          #output 7 