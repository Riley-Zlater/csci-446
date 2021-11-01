from ExactInference import order, normalize

class ApproximateInference():
    def __init__(self):
        pass

    # How sampling works:
    # [0.2, 0.1, 0.3, 0.4] -> 
    # [0.2, (0.2+0.1)=0.3, (0.3+0.3)=0.6, (0.6+0.4)=1] ->
    # [0.2, 0.3, 0.6, 1]
    # generate a random num 0-1
    # if num = 0.55
    # choose element in new list closest to num
    # in this case 0.6
    # so we sample 0.3 (same index as 0.6)

    def markov_blanket(self, variable: list) -> list:
        markov_list = []

        for child in variable.getChildren():
            markov_list.append(child)
            for child_parent in child.getParents():
                markov_list.append(child_parent)

        for parent in variable.getParents():
            markov_list.append(parent)

        return markov_list

    def gibbs_sampling(self, X: object, evidence: list, bayes_net: list, n: int) -> float:
        top_sort_bn = order(bayes_net)
        C = 0
        Z = [var for var in bayes_net if var not in evidence]
        x = None  # Current state of the network

        for k in range(1, n):
            # Choose variable Zi from Z
            # Set the value of Zi in x by sampling from P(Zi|mb(Zi))
            # C[j] <- C[j] + 1 where xj is the value of X in x
            pass

        return normalize(C)
        