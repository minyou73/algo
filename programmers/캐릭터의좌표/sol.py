


    # left = /board =  board[0] + -1
    # right = board = board[0] + 1
    # up = board = board[1] + 1
    # down = board = board[1] - 1



def solution(keyinput, board):


    
    center = [0,0]
    
    for i in keyinput:
        if i == 'up' and center[1] < int(board[1]/2):
            center[1] += 1
        elif i == 'down' and center[1] > -int(board[1]/2) :
            center[1] -= 1
        elif i == 'left' and center[0] > -int(board[0]/2):
            center[0] -= 1
        elif i == 'right'and center[0] < int(board[0]/2):
            center[0] += 1
    
    return center


print(solution(["left", "right", "up", "right", "right"],[11, 11]))

print(solution(["down", "down", "down", "down", "down"], [7,9]))