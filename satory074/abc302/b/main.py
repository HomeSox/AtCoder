def find_snuke(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 's':
                print(i,j )
                for dx, dy in directions:
                    try:
                        if ''.join([grid[i + k * dx][j + k * dy] for k in range(5)]) == 'snuke':
                            return [(i + k * dx, j + k * dy) for k in range(5)]
                    except IndexError:
                        pass
    return []

# Test case
grid = [
    list('s')
]
print(find_snuke(grid))
