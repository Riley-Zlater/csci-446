import numpy as np

def normalize(variable):
    total = None # Sum the row
    if not np.isclose(total, 1.0):
        # for each value in the probability
        # self.prob[val] /= total
        pass
    pass

def markov_blanket(variable):
    markovList = []

    for child in variable.getChildren():
        markovList.append(child)
        for child_parent in child.getParents():
            markovList.append(child_parent)

    for parent in variable.getParents():
        markovList.append(parent)

    return markovList

def gibbs_sampling(variable, evidence, bayes_net, n):
    C = 0
    Z = [var for var in bayes_net if var not in evidence]
    x = None  # Current state of the network

    for k in range(1, n):
        # Choose variable Zi from Z
        # Set the value of Zi in x by sampling from P(Zi|mb(Zi))
        # C[j] <- C[j] + 1 where xj is the value of X in x
        pass

    return normalize(C)
    