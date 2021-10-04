import random
import copy
import math
from LocalSearch import LocalSearch

class GeneticAlgorithm(LocalSearch):
    
    def __init__(self) -> None:
        self.population = []
        self.pop_size = 1000
        self.T = 1
        self.S = .01
        self.h = 0.75
        self.iter = 0
        super().__init__()

    
    def genetic_algorithm(self, puzzle):
        """
        Accepts a sudoku puzzle as input.
        Generates a population of randomized puzzles based on the tuned population size. 
        Iterates through the population determining if a correct solution exists.

        Runs tournament selection on random sets of the population. 

        Accepts two winners of tournament selection and "breeds" them to create
        two new puzzles.

        Randomly mutate the "bred" winners with a low probability to introduce variability
        and help prevent getting stuck at a local maximum.

        Each iteration uses generational replacement to create an entirely new
        population based on the "bred" winners of tournament selection.

        Lower the cooling temperature and increase the Selection pressure for the 
        tournament selection.

        If a solution is found, return the solved puzzle. If not return the best
        puzzle after a predetermined number of iterations.
        """

        for _ in range(0,self.pop_size):
            self.population.append( self.assert_random_values(copy.deepcopy(puzzle)))
        
        

        print("Genetic Alg thinking...")

        best_fit_metric = self.evaluate_fitness(self.population[0]) 
        best_fit = self.population[0]


        while self.T > 0:

            for A in self.population:
                current_fit_metric = self.evaluate_fitness(A)
                if current_fit_metric > best_fit_metric:
                    best_fit_metric = current_fit_metric
                    best_fit = A
                if current_fit_metric == 1.0:
                    return A

            self.iter += 1
            print("Current iteration: " + str(self.iter))
            print("Current Best Fit: " + str(best_fit_metric))
            print()

            new_population = []

            for _ in range(0, int(self.pop_size/2)):
                sample_1 = self.tournament_select()
                sample_2 = self.tournament_select()

                sample_1, sample_2 = self.cross_pollinate(sample_1, sample_2)

                if random.random() < 0.07:
                    sample_1 = self.swap_random(sample_1)

                if random.random() < 0.07:
                    sample_2 = self.swap_random(sample_2)
                
                new_population.append(sample_1)
                new_population.append(sample_2)

            
            self.population = new_population

            self.T -= self.S

        return best_fit
    
    def tournament_select(self):
        """
        Selects a subset of the population based on a random number generator. 
        Compares the values against one another to determine the fittest puzzle.
        Fitter puzzles are accepted with a probability P corresponding to the 
        fitness score and the current Temperature. (The Selection Pressure) The
        Selection pressure increases as the population gets closer to a solution.
        Returns the winning puzzle from the tournament.
        """
        sample_index = random.randint(1,self.pop_size)
        # print(sample_index)

        if sample_index + int(self.pop_size/100) > self.pop_size:
            sample_index = int(self.pop_size - self.pop_size/100 - 1)

        fittest_sample_value = self.evaluate_fitness(self.population[sample_index])
        fittest_sample = self.population[sample_index]

        for i in range(sample_index, int(sample_index+self.pop_size/100 - 1)):
            f_s = self.evaluate_fitness(self.population[i])
            if f_s > fittest_sample_value and random.random() > math.exp((-self.h*f_s)/self.T):
                fittest_sample_value = f_s
                fittest_sample = self.population[i]
                
        return fittest_sample
    
    def evaluate_fitness(self, puzzle):
        """
        Accepts a sudoku puzzle as input.
        Generates a fitness heuristic corresponding to
        how many duplicate values exist in each column. 
        If duplicates exist in a row/column it scores lower than
        9. If duplicates do not exist the row/column scores a 9.
        The final score for all rows and columns is added and
        divided by 162 (The potential max score). To
        determine the puzzle's fitness score.
        Returns a fitness score.
        """
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
        """
        Accepts two sudoku puzzles as inputs.
        Generates a selection for the subsqare of both puzzles.
        Swaps a value from each puzzle with the other. 
        Corrects duplicates created from value swapping.
        Returns two updated puzzles.
        """
        sample_1_copy = copy.deepcopy(sample_1)
        sample_2_copy = copy.deepcopy(sample_2)

        # for _ in range(0,3):

        r_sector = 3 * random.randint(0,2)
        c_sector = 3 * random.randint(0,2)

        r1 = self.generate_randoms(r_sector, c_sector)
        r2 = self.generate_randoms(r_sector, c_sector)

        if r1 in self.fixed_values:
            print("r1 in fixed values")
        
        if r2 in self.fixed_values:
            print("r2 in fixed values")

        temp = sample_1_copy[r1[0]][r1[1]]
        sample_1_copy[r1[0]][r1[1]] = sample_2_copy[r2[0]][r2[1]]
        sample_2_copy[r2[0]][r2[1]] = temp

        sample_1_copy, sample_2_copy = self.correct_sub_box(sample_1_copy, sample_2_copy, r_sector, c_sector,  r1, r2)

        return sample_1_copy, sample_2_copy

    def correct_sub_box(self, s1, s2, r_s, c_s, r1, r2):
        """
        Accepts two sudoku puzzles, a row sector and column sector value, and
        indices for swapping. 
        Uses the swapped indices to identify the value for which a duplicate
        may exist.
        Swaps puzzle 1's duplicate value for puzzle 2's duplicate value.
        Returns two updated puzzles
        """
        val1 = s1[r1[0]][r1[1]]
        val2 = s2[r2[0]][r2[1]]

        valid_1 = None
        valid_2 = None

        for i in range(r_s, r_s+3):
            for j in range(c_s, c_s+3):
                if val1 == s1[i][j] and [i,j] != r1:
                    if valid_1 is not None:
                        break
                    valid_1 = [i,j]

        for i in range(r_s, r_s+3):
            for j in range(c_s, c_s+3):
                if val2 == s2[i][j] and [i,j] != r2:
                    if valid_2 is not None:
                        break
                    valid_2 = [i,j]
                    
        if valid_1 in self.fixed_values:
            print("valid 1 in fixed values")
        
        if valid_2 in self.fixed_values:
            print("valid 2 in fixed values")

        if valid_1 is not None and valid_2 is not None:
            temp = s1[valid_1[0]][valid_1[1]]
            s1[valid_1[0]][valid_1[1]] = s2[valid_2[0]][valid_2[1]]
            s2[valid_2[0]][valid_2[1]] = temp


        return s1, s2