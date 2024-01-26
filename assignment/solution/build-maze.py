import random

# A-maze-ing

def create_maze(rows, cols, wall, path):
    maze = [[wall for _ in range(cols)] for _ in range(rows)]

    stack = [(0,0)]
    maze[0][0] = path

    dirs = [(0,-2), (0,2), (-2,0), (2,0)]

    while stack:
        row, col = stack[-1]
        random.shuffle(dirs)

        for dr, dc in dirs:
            nrow, ncol = row + dr, col + dc

            if 0 <= nrow < rows and 0 <= ncol < cols and maze[nrow][ncol] == wall:
                maze[row + dr // 2][col + dc // 2] = path
                maze[nrow][ncol] = path
                stack.append((nrow, ncol))
                break
        else:
            stack.pop()

    maze = [[wall] * rows] + maze + [[wall] * rows]
    maze =[[wall]+m+[wall] for m in maze]

    maze[rows][cols+1] = path
    maze[1][0] = path

    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(map(str, row)))

rows, cols = 31, 31
maze = create_maze(rows, cols, wall = '#', path = ' ')
print_maze(maze)


start = (1,0)
end = (rows, cols+1)
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

queue = [start]

while queue:
    next = queue.pop(0)

    row, col = next
    maze[row][col] = '*'

    if next == end:
        break
    
    for dr, dc in dirs:
        nrow, ncol = row+dr, col+dc

        if 0 <= nrow < rows+2 and 0 <= ncol < cols+2 and maze[nrow][ncol] == ' ':
            queue.append((nrow,ncol))

print_maze(maze)


