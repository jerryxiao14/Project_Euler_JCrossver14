grid = []
for _ in range(20):
    grid.append(list(map(int,input().split())))


max_product = 0
for i in range(20):
    for j in range(20):
        # Horizontal
        if j + 3 < 20:
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if product > max_product:
                max_product = product
        # Vertical
        if i + 3 < 20:
            product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if product > max_product:
                max_product = product
        # Diagonal down-right
        if i + 3 < 20 and j + 3 < 20:
            product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if product > max_product:
                max_product = product
        # Diagonal down-left
        if i + 3 < 20 and j - 3 >= 0:
            product = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
            if product > max_product:
                max_product = product
print(max_product)