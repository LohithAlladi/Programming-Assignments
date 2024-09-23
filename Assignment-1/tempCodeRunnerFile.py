def is_valid_move(self, x : int, y : int, rows : int, cols : int) -> bool:
    if(x < 0 or x >= rows ):
        return False
    elif(y < 0 or y >= cols):
        return False
    elif(self.navigator_maze[x][y] == 1):
        return False
    return True