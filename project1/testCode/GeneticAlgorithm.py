import random
from LocalSearch import LocalSearch

class GeneticAlgorithm(LocalSearch):
    
    def __init__(self) -> None:
        self.population = dict()
        super().__init__()

    
    def genetic_algorithm(self, puzzle):

        for i in range(0,10000):
            self.population[i] = self.assert_random_values(puzzle)

        sample_1 = self.tournament_select()
        sample_2 = self.tournament_select()

        new_sample = self.cross_pollinate(sample_1, sample_2)

        fitness = self.evaluate_fitness(puzzle)

        print(puzzle)
        return fitness
    
    def tournament_select(self):
        sample = random.randint(0,9999)

        if sample + 100 > 9999:
            sample = 9899

        fittest_sample = self.population[sample]

        for i in range(sample, sample+100):
            f_s = self.evaluate_fitness(self.population[i])
            if f_s > fittest_sample:
                fittest_sample = f_s
        
        return fittest_sample
    
    def evaluate_fitness(self, puzzle):
        row_fit = 0
        col_fit = 0

        for x in range(0,9):
            row_dups = dict()
            for y in range(0,9):
                if puzzle[x][y] not in row_dups:
                    row_fit += 1
                row_dups[puzzle[x][y]] = 1
        
        for x in range(0,9):
            col_dups = dict()
            for y in range(0,9):
                if puzzle[y][x] in col_dups:
                    col_fit += 1
                col_dups[puzzle[y][x]] = 1

        return (row_fit + col_fit) / 162
            
    
    def cross_pollinate(self, sample_1, sample_2):
        return