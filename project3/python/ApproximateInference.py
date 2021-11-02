from ExactInference import order
import numpy as np
import random as ran

class ApproximateInference():
    def __init__(self) -> None:
        pass

    def norm(self, data: list) -> list:
        return [x / sum(data) for x in data]

    def sample(self, variable: object) -> float:
        variable_values = variable.getProbabilityTable().values()
        variable_values = variable_values[ran.randint(1, len(variable_values))]
        return ran.choices(variable_values, variable_values)

    def markov_blanket(self, variable: object) -> list:
        markov_list = []

        for child in variable.getChildren():
            markov_list.append(child)
            for child_parent in child.getParents():
                markov_list.append(child_parent)

        for parent in variable.getParents():
            markov_list.append(parent)
        return markov_list

    def gibbs_sampling(self, X: object, evidence: list, bayes_net: list, num_iter: int) -> list:
        top_sort_bn = order(bayes_net)
        C = []
        Z = [var for var in bayes_net if var not in evidence]
        x = evidence  # Current state of the network

        for k in range(1, num_iter):
            Z_k = ran.choice(Z)
            # Set the value of Zi in x by sampling from P(Zi|mb(Zi))
            # C[j] <- C[j] + 1 where xj is the value of X in x
        return self.norm(C) # Normalize C
        