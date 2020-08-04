import time

def solve(bo):
    find = find_empty(bo)
    if not find:  # if find is None or False
        # print(bo)
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column

    return None


start = time.time()

# Using readlines() 
file1 = open('sudoku.txt', 'r') 
lines = file1.readlines()
sudoku_solutions_file = open('sudoku_solutions.txt', 'w') 
# Initialising some variables
board = []
row = []
solved_board = []
grid_name = ""
count = 1

for line in lines:
    line = line.strip()
    
    if "Grid" in line:
        grid_name = line
        # total_values.append(grid_name)
    else:
        for char in line:
            row.append(int(char))
        # print(row)
        board.append(row)
        count +=1
        row = []
        
        if count == 10:
            count = 1
            solve(board)
            # writing to file 
            sudoku_solutions_file.writelines(grid_name + "\n")
            # Need to convert each board line into a string to write in the file
            for line in board:
                line = ''.join(map(str, line))
                sudoku_solutions_file.writelines(line + '\n')
            
            board = []
            
            
sudoku_solutions_file.close() 

end = time.time()
print(end - start)