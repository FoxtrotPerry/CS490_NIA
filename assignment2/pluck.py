import sys
import math

class pnd_solver(object):
    def __init__(self, path):
        raw_file = open(path,'r').read().split('\n')
        rows = [list(map(int, line.split())) for line in raw_file if line]
        self.operation_string = ""
        self.operation_cnt, self.robot_location, self.holding_block, self.finished, self.dirty = 0, 0, False, False, False
        self.num_rows, self.current_stack, self.end_stack = rows[0][0], rows[1], rows[2]

    def pluck(self):
        if(self.holding_block == False):
            self.current_stack[self.robot_location] -= 1
            self.operation_cnt += 1
            self.operation_string += "P"
            self.holding_block = True
            self.dirty = True

    def drop(self):
        if(self.holding_block == True):
            self.current_stack[self.robot_location] += 1
            self.operation_cnt += 1
            self.operation_string += "D"
            self.holding_block = False
            self.dirty = True

    def move_left(self):
        self.robot_location -= 1
        self.operation_string += "L"
        self.operation_cnt += 1

    def move_right(self):
        self.robot_location += 1
        self.operation_string += "R"
        self.operation_cnt += 1

    def fitness(self):
        final_fitness = 0
        for i in range(0, self.num_rows):
            final_fitness += pow(abs(self.current_stack[i]-self.end_stack[i]),3)
        print("Fitness val w/o op_count: " + str(final_fitness))
        return final_fitness + self.operation_cnt

    def column_delta(self):
        return self.current_stack[self.robot_location] - self.end_stack[self.robot_location]

    def determ(self):
        while(not self.finished):
            self.dirty = False
            for i in range(0, self.num_rows-1):
                column_delta = self.column_delta()
                if column_delta > 0:
                    self.pluck()
                elif column_delta < 0:
                    self.drop()
                self.move_right()

            for i in range(0, self.num_rows-1):
                column_delta = self.column_delta()
                if column_delta > 0:
                    self.pluck()
                elif column_delta < 0:
                    self.drop()
                self.move_left()

            if(not self.dirty and not self.holding_block):
                self.finished = True

        print("Finished after " + str(self.operation_cnt) + " operations.")
        return self.fitness()

stack_set_det = pnd_solver(sys.argv[1])
stack_set_sto = pnd_solver(sys.argv[1])
print(stack_set_det.fitness())
print(stack_set_det.determ())
print("Current stack: " + str(stack_set_det.current_stack) + "\n" + "  Final stack: " + str(stack_set_det.end_stack))
print("Operation String: " + stack_set_det.operation_string)
