# def find_xmas(grid):
#     count = 0
#     rows = len(grid)
#     cols = len(grid[0])
#
#     # Directions for moving in the grid: right, down, diagonals, and their reverse counterparts
#     directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
#
#     for r in range(rows):
#         for c in range(cols):
#             for dr, dc in directions:
#                 if check_word(grid, r, c, dr, dc, 'XMAS'):
#                     count += 1
#     return count
#
# def check_word(grid, r, c, dr, dc, word):
#     rows = len(grid)
#     cols = len(grid[0])
#     for i in range(len(word)):
#         nr, nc = r + i * dr, c + i * dc
#         if 0 <= nr < rows and 0 <= nc < cols:
#             if grid[nr][nc] != word[i]:
#                 return False
#         else:
#             return False
#     return True
#
# def read_grid(file_path):
#     with open(file_path, 'r') as file:
#         grid = [line.strip() for line in file.readlines()]
#     return grid
#
# # Input file path
# file_path = 'input.txt'
#
# grid = read_grid(file_path)
# print(find_xmas(grid))

def count_xmas_patterns(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Define all possible X-MAS patterns
    x_mas_patterns = [
        ((0, 0), (2, 0), (1, 1)), # Forward "MAS" in X
        ((0, 0), (2, 0), (1, -1)), # Forward "MAS" in reverse X
        ((0, 0), (0, 2), (1, 1)), # Forward "MAS" in horizontal X
        ((0, 0), (0, 2), (-1, 1)), # Forward "MAS" in horizontal reverse X
        ((0, 0), (-2, 0), (-1, 1)), # Backward "MAS" in X
        ((0, 0), (-2, 0), (-1, -1)), # Backward "MAS" in reverse X
        ((0, 0), (0, -2), (1, -1)), # Backward "MAS" in horizontal X
        ((0, 0), (0, -2), (-1, -1)) # Backward "MAS" in horizontal reverse X
    ]

    def check_pattern(grid, r, c, pattern):
        try:
            return (
                grid[r + pattern[0][0]][c + pattern[0][1]] == 'M' and
                grid[r + pattern[1][0]][c + pattern[1][1]] == 'S' and
                grid[r + pattern[2][0]][c + pattern[2][1]] == 'A'
            )
        except IndexError:
            return False

    for r in range(rows):
        for c in range(cols):
            for pattern in x_mas_patterns:
                if check_pattern(grid, r, c, pattern):
                    count += 1
    return count

def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

file_path = 'input.txt'

grid = read_grid(file_path)
print(count_xmas_patterns(grid))

