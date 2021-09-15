import random
import copy
from LocalSearch import LocalSearch

class GeneticAlgorithm(LocalSearch):
    
    def __init__(self) -> None:
        self.population = []
        self.pop_size = 1000
        super().__init__()

    
    def genetic_algorithm(self, puzzle):

        for i in range(0,self.pop_size):
            self.population.append( self.assert_random_values(puzzle))

        while True:

            best_fit = self.evaluate_fitness(self.population[0])
            iter = 0

            for A in self.population:
                if self.evaluate_fitness(A) > best_fit:
                    best_fit = self.evaluate_fitness(A)
                if self.evaluate_fitness(A) == 1.0:
                    return A
            iter += 1
            print("Current iteration: " + str(iter))
            print("Current Best Fit: " + str(best_fit))

            new_population = []

            for k in range(0, int(self.pop_size/2)):
                print("Generating samples")
                sample_1 = self.tournament_select()
                sample_2 = self.tournament_select()

                print("Cross pollination or whatever")
                sample_1, sample_2 = self.cross_pollinate(sample_1, sample_2)

                print("Appending to new pop")
                new_population.append(sample_1, sample_2)

                # print(self.evaluate_fitness(sample_1))
            
            self.population = new_population

            # return fitness
    
    def tournament_select(self):
        sample_index = random.randint(1,self.pop_size)

        if sample_index + 10 > self.pop_size:
            sample_index = 989

        fittest_sample = self.evaluate_fitness(self.population[sample_index])

        for i in range(sample_index, sample_index+10):
            f_s = self.evaluate_fitness(self.population[i])
            if f_s > fittest_sample:
                fittest_sample = f_s
        
        print("found fittest sample")
        
        return fittest_sample
    
    def evaluate_fitness(self, puzzle):
        row_fit = 0
        col_fit = 0

        for x in range(0,9):
            row_dups = []
            for y in range(0,9):
                if puzzle[x][y] not in row_dups:
                    row_fit += 1
                row_dups.append(puzzle[x][y])
        
        for x in range(0,9):
            col_dups = []
            for y in range(0,9):
                if puzzle[y][x] not in col_dups:
                    col_fit += 1
                col_dups.append(puzzle[y][x])

        return (row_fit + col_fit) / 162
            
    
    def cross_pollinate(self, sample_1, sample_2):
        sample_1_copy = copy.deepcopy(sample_1)
        sample_2_copy = copy.deepcopy(sample_2)

        r_sector = 3 * random.randint(0,2)
        c_sector = 3 * random.randint(0,2)

        print("About to generate randoms")

        r1 = self.generate_randoms(r_sector, c_sector)
        print(r1)
        r2 = self.generate_randoms(r_sector, c_sector)
        print(r2)
        
        print("generated randoms")

        temp = sample_1_copy[r1[0]][r1[1]]
        sample_1_copy[r1[0]][r1[1]] = sample_2_copy[r2[0]][r2[1]]
        sample_2_copy[r2[0]][r2[1]] = temp

        sample_1_copy, sample_2_copy = self.correct_sub_box(sample_1_copy, sample_2_copy, r_sector, c_sector,  r1, r2)

        return

    def correct_sub_box(self, s1, s2, r_s, c_s, r1, r2):
        val1 = s1[r1[0]][r1[1]]
        val2 = s2[r2[0]][r2[1]]

        for i in range(r_s, r_s+3):
            for j in range(c_s, c_s+3):
                if val1 is s1[i][j] and [i,j] != r1:
                    r1 = [i,j]

        for i in range(r_s, r_s+3):
            for j in range(c_s, c_s+3):
                if val2 is s2[i][j] and [i,j] != r2:
                    r2 = [i,j]
        
        temp = s1[r1[0]][r1[1]]
        s1[r1[0]][r1[1]] = s2[r2[0]][r2[1]]
        s2[r2[0]][r2[1]] = temp

        return s1, s2