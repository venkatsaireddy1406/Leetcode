def main(board):
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            # Check rows
            if board[i][j] != '.':
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])

            # Check columns
            if board[j][i] != '.':
                if board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])

    # Check 3x3 sub-boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box_set = set()
            for m in range(3):
                for n in range(3):
                    if board[i + m][j + n] != '.':
                        if board[i + m][j + n] in sub_box_set:
                            return False
                        sub_box_set.add(board[i + m][j + n])

    return True
    

if __name__=="__main__":
    print(main(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))