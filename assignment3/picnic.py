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
        self.candidate = np.full([self.dimm_val,self.dimm_val,2],-1)
        # print(self.candidate)

    def doTabuSearch(self):
        self.print_dominoes()
        # TODO: Initialize the candidate with random dominoes
        # TODO: Make while loop for algorithm with iterator count
        # TODO: Make tabu_list element addition qualification logic
        # TODO: Make next step logic for candidate based on contents of tabu_list
        # TODO: Make finish logic for if fitness is 0. print iteration count as well.

    def fitness(self):
        # Rules:
        # 1. Each number missing from a row or column is one violation
        # 2. Each pairing that is duplicated is one violation
        score = 0 #hopefully stays at zero...
        for i in range(0,self.dimm_val):
            # print("Calcing for: " + str(i))
            score = score + self.row_search(i) + self.col_search(i)
        print("Fitness: " + str(score))
        return score
 
    def row_search(self,search_row):
        unique_dominoes = set()
        unique_acc = set()
        all_acc = []
        for i in range(0,self.dimm_val):
            unique_acc.add(self.candidate[search_row][i][0])
            unique_acc.add(self.candidate[search_row][i][1])
            new_item = [self.candidate[search_row][i][0], self.candidate[search_row][i][1]]
            all_acc.append(tuple(sorted(new_item)))
        unique_acc.discard(-1)
        # Rule 1 violations:
        missing_ints = self.max_teams - len(unique_acc)
        # Rule 2 violations:
        for i in range(0,self.dimm_val):
            unique_dominoes.add(all_acc[i])

        return missing_ints + (self.dimm_val - len(unique_dominoes))
        
    def col_search(self,search_col):
        unique_dominoes = set()
        unique_acc = set()
        all_acc = []
        for i in range(0,self.dimm_val):
            unique_acc.add(self.candidate[i][search_col][0])
            unique_acc.add(self.candidate[i][search_col][1])
            new_item = [self.candidate[i][search_col][0], self.candidate[i][search_col][1]]
            all_acc.append(tuple(sorted(new_item)))
        unique_acc.discard(-1)
        # Rule 1 violations:
        missing_ints = self.max_teams - len(unique_acc)
        # Rule 2 violations:
        for i in range(0,self.dimm_val):
            unique_dominoes.add(all_acc[i])

        return missing_ints + (self.dimm_val - len(unique_dominoes))
    
    def print_dominoes(self):
        for i in range(0,self.dimm_val):
            for j in range(0,self.dimm_val):
                print(str(self.candidate[i][j][0]) + ":" + str(self.candidate[i][j][1]), end=' ')
            print()

picnic3 = picnic(3)
picnic8 = picnic(8)
picnic3.doTabuSearch()
picnic3.fitness()
picnic8.doTabuSearch()
picnic8.fitness()
#picnic.print_dominoes()
