def print_maze(maze,x,y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print s
    print ' '

class MazeRunner(object):
    
    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        return True
    
    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self
    
    def turn_right(self):
        right_rotation = {
            (1,0): (0,1),
            (0,-1): (1,0),
            (-1,0): (0,-1),
            (0,1): (-1,0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self
    
    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]

def maze_controller(mr):
    mr.found()
    if mr.found():
        mr.go()
    else:
        mr.turn_left()
        mr.found()
        if mr.found():
            mr.go()
        else:
            mr.turn_left()
            mr.found()
            if mr.found():
               mr.go()
            else:
                mr.turn_left()
                mr.found()
                if mr.found():
                    mr.go()
                mr.turn_left()
                mr.go()
                if mr.go():
                    return maze_controller(mr)
                else:
                    mr.turn_left()
                    mr.go()
                    if mr.go():
                        return maze_controller(mr)
                    else:
                        mr.turn_right()
                        mr.turn_right()
                        mr.go()
                        if mr.go():
                            return maze_controller(mr)
                        else:
                            mr.turn_right()
                            mr.go()
                            return maze_controller(mr)
                
                
maze_example1 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}
maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(maze_runner)
print maze_runner.found()
