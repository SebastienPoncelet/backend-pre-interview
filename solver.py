

def solve(board):
    """
    Method testing each empty cell's value and replacing correct values in board
    """
    find = find_empty(board)
    if not find:  # if find is None or False
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, coordinates):
    """
    Method checking if cell's value already exists in either it's row, column or box
    """
    # Check row
    for i in range(len(board[0])):
        if board[coordinates[0]][i] == num and coordinates[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][coordinates[1]] == num and coordinates[0] != i:
            return False

    # Check box
    box_x = coordinates[1] // 3
    box_y = coordinates[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != coordinates:
                return False

    return True


def find_empty(board):
    """
    Method looking for coordinates of empty cells (equal to 0 in text file)
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, column

    return None


# Open file to read data from
file1 = open('sudoku.txt', 'r') 
lines = file1.readlines()
# Create and open file to write solutions to
sudoku_solutions_file = open('sudoku_solutions.txt', 'w') 
# Initialising some variables
board = []
row = []
grid_name = ""
count = 1

# Extracting grids from text file using readlines() 
for line in lines:
    line = line.strip() #
    
    if "Grid" in line:
        grid_name = line
    else:
        #convert each string from the grid into an integer and add it to its row's list
        for char in line:
            row.append(int(char)) 
        
        board.append(row) # Add each row to the board
        count += 1
        row = []
        
        # If the count reaches 10 then the board is complete
        if count == 10:
            count = 1
            # Call on function to solve the grid
            solve(board)
            # writing to file 
            sudoku_solutions_file.writelines(grid_name + "\n")
            # Need to convert each board line into a string to write in the file
            for line in board:
                line = ''.join(map(str, line))
                sudoku_solutions_file.writelines(line + '\n')
                
            sudoku_solutions_file.writelines(
                "The sum of " +  grid_name + "'s first three numbers is of: " + 
                str(sum(board[0][:3])) + 
                "\n")
            
            board = []
            
# Once all solutions have been found, close the writing file
sudoku_solutions_file.close()