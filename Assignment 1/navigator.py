from maze import *
from exception import *
from stack import *
import copy

class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
        
    def find_path(self, start : tuple[int, int], end : tuple[int, int]) -> list[tuple[int, int]]:
        # IMPLEMENT FUNCTION HERE
        recover = copy.deepcopy(self.navigator_maze)
        rows = len(self.navigator_maze)
        cols = len(self.navigator_maze[0])
        stack = Stack()
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        x, y = start[0], start[1]
        stack.push((x,y))
        recover[x][y] = 1
        while((x,y)!=end):
                for move in moves:
                    x, y = stack.top()[0] + move[0], stack.top()[1] + move[1]
                    if (self.is_valid_move(x,y,rows,cols,recover)):
                        stack.push((x,y))
                        recover[x][y] = 1   
                        break
                else:
                    stack.pop()
                    if (not stack.is_empty()):
                        x, y = stack.top()[0], stack.top()[1]
                    else:
                        break
        if not stack.is_empty():
            return stack.list 
                           
        raise PathNotFoundException
        
    def is_valid_move(self, x : int, y : int, rows : int, cols : int, recover) -> bool:
        if(x < 0 or x >= rows ):
            return False
        elif(y < 0 or y >= cols):
            return False
        elif(recover[x][y] == 1):
            return False
        return True