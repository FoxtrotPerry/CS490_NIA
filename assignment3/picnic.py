import numpy as np 
# sudo pip install numpy
# python3 version: python3 -m pip install numpy

class picnic(object):
    def __init__(self, dimm_val):
        self.dimm_val = dimm_val
        self.max_teams = dimm_val * 2
        self.tabu_list = []

        self.all_dominoes = np.zeros([self.max_teams**2,2], dtype=int)
        for i in range(0,self.max_teams):
            for j in range(0,self.max_teams):
                pos = (i*self.max_teams+j)
                self.all_dominoes[pos] = self.all_dominoes[pos] + [i,pos%self.max_teams]
        self.current_dominoes = np.full([self.dimm_val,self.dimm_val,2],-1)
        print(self.current_dominoes)
    
    def fitness(self):
        self.score = 0 #hopefully stays at zero...
        self.score = self.row_search(0,0) + self.col_search(0,0)
        print("Fitness: " + str(self.score))

    def row_search(self,search_row,target_num):
        row_score = self.max_teams
        unique_acc = set()
        for i in range(0,self.dimm_val):
            unique_acc.add(self.current_dominoes[search_row][i][0])
            unique_acc.add(self.current_dominoes[search_row][i][1])
        unique_acc.discard(-1)
        row_score = row_score - len(unique_acc)
        return row_score
        
    def col_search(self,search_col,target_num):
        col_score = self.max_teams
        unique_acc = set()
        for i in range(0,self.dimm_val):
            unique_acc.add(self.current_dominoes[i][search_col][0])
            unique_acc.add(self.current_dominoes[i][search_col][1])
        unique_acc.discard(-1)
        col_score = col_score - len(unique_acc)
        return col_score

picnic = picnic(3)
picnic.fitness()
