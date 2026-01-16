grid = []
while True:
    try:
        grid.append(list(map(int,input().split())))
    except EOFError:
        break 

dp = [[0 for _ in range(len(grid[i]))] for i in range(len(grid))]
dp[0][0] = grid[0][0]
for i in range(1,len(grid)):
    dp[i][0] = dp[i-1][0]+grid[i][0]
    for j in range(1,len(grid[i])-1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+grid[i][j]
    dp[i][-1] = dp[i-1][-1]+grid[i][-1]
print(max(dp[-1]))