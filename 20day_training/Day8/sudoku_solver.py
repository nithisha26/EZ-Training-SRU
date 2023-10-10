def solve(s):
    if s==81:
        return True
    row=s//9
    col=s%9
    if board[row][col]!='.':
        solve(s+1)
    for i in "123456789":
        if isvalid(i,row,col):
            board[row][col]=i
            solve(j+1)
        board[row][col]='.'
