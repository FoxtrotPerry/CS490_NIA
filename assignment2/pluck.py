import sys
import math

class pnd_solver(object):
    def __init__(self, path):
        raw_file = open(path,'r').read().split('\n')
        rows = [list(map(int, line.split())) for line in raw_file if line]
        self.operation_cnt, self.robot_location = 0, 0
        self.num_rows, self.current_stack, self.end_stack = rows[0][0], rows[1], rows[2]

    def pluck(self):
        self.current_stack[self.robot_location] -= 1
        self.operation_cnt += 1

    def drop(self):
        self.current_stack[self.robot_location] += 1
        self.operation_cnt += 1

    def move_left(self):
        self.robot_location -= 1
        self.operation_cnt += 1

    def move_right(self):
        self.robot_location += 1
        self.operation_cnt += 1

    def fitness():
        final_fitness = operation_cnt
        for i in range(0, self.num_rows):
            final_fitness += pow(abs(current_stack[i]-end_stack[i]),3)

    def get_stack_height(self,i):

object = pnd_solver(sys.argv[1])



