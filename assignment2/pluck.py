import sys
import math
import random
from itertools import chain

# To see where the max amount of plays is derived from, refer to this plot: https://www.desmos.com/calculator/snls1lpu4w

class pnd_solver(object):
    def __init__(self, path):
        raw_file = open(path,'r').read().split('\n')
        columns = [list(map(int, line.split())) for line in raw_file if line]
        self.operation_string = ""
        self.robot_location, self.holding_block, self.finished, self.dirty = 0, False, False, False
        self.num_columns, self.start_stack, self.current_stack, self.end_stack = columns[0][0], columns[1], columns[1], columns[2]

    def pluck(self):
        if(self.holding_block == False and self.current_stack[self.robot_location] != 0):
            self.current_stack[self.robot_location] -= 1
            self.operation_string += "P"
            self.holding_block = True
            self.dirty = True

    def drop(self):
        if(self.holding_block == True):
            self.current_stack[self.robot_location] += 1
            self.operation_string += "D"
            self.holding_block = False
            self.dirty = True

    def move_left(self):
        self.robot_location -= 1
        self.operation_string += "L"

    def move_right(self):
        self.robot_location += 1
        self.operation_string += "R"


    def fitness(self):
        final_fitness = 0
        for i in range(0, self.num_columns):
            final_fitness += pow(abs(self.current_stack[i]-self.end_stack[i]),3)
        return final_fitness + len(self.operation_string)

    def column_delta(self):
        return self.current_stack[self.robot_location] - self.end_stack[self.robot_location]

    def reset(self):
        self.current_stack = self.start_stack
        self.operation_string = ""

    def determ(self):
        while(not self.finished):
            self.dirty = False
            for i in range(0, self.num_columns-1):
                column_delta = self.column_delta()
                if column_delta > 0:
                    self.pluck()
                elif column_delta < 0:
                    self.drop()
                self.move_right()

            for i in range(0, self.num_columns-1):
                column_delta = self.column_delta()
                if column_delta > 0:
                    self.pluck()
                elif column_delta < 0:
                    self.drop()
                self.move_left()

            if(not self.dirty and not self.holding_block):
                self.finished = True
        while("LR" in self.operation_string and "RL" in self.operation_string):
            self.operation_string = self.operation_string.replace("LR","")
            self.operation_string = self.operation_string.replace("RL","")
        last_drop_index = self.operation_string.rfind('D')
        self.operation_string = self.operation_string[0:last_drop_index+1]

        print("Finished after " + str(len(self.operation_string)) + " operations.")
        return self.fitness()

    def LRS(self, iterations):
        recommended_play_num = int(6.25952*self.num_columns + 1.2*self.num_columns)
        chunks = 4
        chunk_length = int(recommended_play_num/4)
        iteration_index = 0
        chunk_array, chunk_best_fits = [[],[],[],[]], [0,0,0,0]
        chunk_index = 0
        while(chunk_index!=chunks):
            if(chunk_index==0):
                for i in range(0,int(iterations/4)):
                    self.reset()
                    operation_ints = self.generate_int_list(chunk_length)
                    op_ints = self.doLRSactions(operation_ints)
                    chunk_fit = self.fitness()
                    if(chunk_fit < chunk_best_fits[chunk_index] or chunk_best_fits[chunk_index] == 0):
                        chunk_best_fits[chunk_index] = chunk_fit
                        chunk_array[chunk_index] = operation_ints
                    iteration_index+=1

            elif(chunk_index==1):
                for i in range(0,int(iterations/4)):
                    self.reset()
                    operation_ints = self.generate_int_list(chunk_length)
                    op_ints = self.doLRSactions(chunk_array[0] + operation_ints)
                    chunk_fit = self.fitness()
                    if(chunk_fit < chunk_best_fits[chunk_index] or chunk_best_fits[chunk_index] == 0):
                        chunk_best_fits[chunk_index] = chunk_fit
                        chunk_array[chunk_index] = operation_ints
                    iteration_index+=1

            elif(chunk_index==2):
                for i in range(0,int(iterations/4)):
                    self.reset()
                    operation_ints = self.generate_int_list(chunk_length)
                    op_ints = self.doLRSactions(chunk_array[0] + chunk_array[1] + operation_ints)
                    chunk_fit = self.fitness()
                    if(chunk_fit < chunk_best_fits[chunk_index] or chunk_best_fits[chunk_index] == 0):
                        chunk_best_fits[chunk_index] = chunk_fit
                        chunk_array[chunk_index] = operation_ints
                    iteration_index+=1

            elif(chunk_index==3):
                for i in range(0,int(iterations/4)):
                    self.reset()
                    operation_ints = self.generate_int_list(chunk_length)
                    op_ints = self.doLRSactions(chunk_array[0] + chunk_array[1] + chunk_array[2] + operation_ints)
                    chunk_fit = self.fitness()
                    if(chunk_fit < chunk_best_fits[chunk_index] or chunk_best_fits[chunk_index] == 0):
                        chunk_best_fits[chunk_index] = chunk_fit
                        chunk_array[chunk_index] = operation_ints
                    iteration_index+=1
            chunk_index+=1
        chunk_best_fit, chunk_best_fit_index = 0, 0
        best_op_ints = []
        for i in range(0,int(len(chunk_best_fits))):
            if(chunk_best_fits[i]<chunk_best_fit or chunk_best_fit==0):
                chunk_best_fit = chunk_best_fits[i]
                chunk_best_fit_index = i
        print("Best fit: " + str(chunk_best_fit))
        for i in range(0,chunk_best_fit_index+1): 
            best_op_ints += chunk_array[i]
        print("Best op ints: " + str(best_op_ints))
        self.reset()
        self.doLRSactions(best_op_ints)
        self.fitness()

    def doLRSactions(self, int_list):
        for i in range(0,len(int_list)-1):
            robot_pos_delta = self.robot_location-int_list[i]
            if(i%2==0):
                while(robot_pos_delta>0):
                    self.move_left()
                    robot_pos_delta-=1
                while(robot_pos_delta<0):
                    self.move_right()
                    robot_pos_delta+=1
                self.pluck()
            else:
                while(robot_pos_delta>0):
                    self.move_left()
                    robot_pos_delta-=1
                while(robot_pos_delta<0):
                    self.move_right()
                    robot_pos_delta+=1
                self.drop()
        return int_list

    def generate_int_list(self, recommended_play_num):
        operation_ints = [random.randint(0,self.num_columns-1)]
        for i in range(0,2*recommended_play_num-2):
            rand_int = random.randint(0,self.num_columns-1)
            while(operation_ints[i]==rand_int):
                rand_int = random.randint(0,self.num_columns-1)
            operation_ints.append(rand_int)
        return operation_ints

stack_set_det = pnd_solver(sys.argv[1])
stack_set_sto3 = pnd_solver(sys.argv[1])
stack_set_sto4 = pnd_solver(sys.argv[1])
stack_set_sto5 = pnd_solver(sys.argv[1])

print("============= DETERMINISTIC =============")
print(stack_set_det.determ())
print("Operation String: " + stack_set_det.operation_string + "X")
print("================== LRS ==================")
stack_set_sto3.LRS(10**3)
print("Operation String for 10^3: " + stack_set_sto3.operation_string + "X")
print()
stack_set_sto4.LRS(10**4)
print("Operation String for 10^4: " + stack_set_sto4.operation_string + "X")
print()
stack_set_sto5.LRS(10**5)
print("Operation String for 10^5: " + stack_set_sto5.operation_string + "X")
print()

