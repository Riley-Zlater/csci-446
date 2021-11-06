import random as ran

class ApproximateInference():  # Remove from a Class?
    def __init__(self) -> None:
        pass

    def norm(self, data: list) -> list:
        return [x / sum(data) for x in data]

    def sample(self, variable: object) -> list & float & int:
        variable_key_tuple = variable.getProbabilityTable().keys()
        ran_key = list(variable_key_tuple)[ran.randint(0, len(variable_key_tuple)-1)]
        ran_value_index = ran.randint(0, len(variable.getProbabilityTable()[ran_key])-1)
        ran_value = variable.getProbabilityTable()[ran_key][ran_value_index]

        variable.setCurrentState(variable.getVarTypes()[ran_value_index])

        
        return ran_key, ran_value, ran_value_index

    def markov_blanket(self, variable: object) -> list:
        markov_list = []

        for child in variable.getChildren():
            markov_list.append(child)
            for child_parent in child.getParents():
                markov_list.append(child_parent)

        for parent in variable.getParents():
            markov_list.append(parent)
        return markov_list

    def getState(self, variable: object, sample_key: float) -> list:
        sample = list()
        
        sample.append(sample_key)
        sample.append(variable.getCurrentState())

        return sample

    def gibbs_sampling(self, X: object, evidence: list, bayes_net: list, num_iter: int) -> list:
        C = []  # Count of variable you're encountering
        Z = [var for var in bayes_net if var not in evidence and not X]  # Hiden variables (all vars that are not evidence or the query)
        x = evidence  # Current state of the network (the value of the variable currently?)

        for k in range(1, num_iter):
            Z_k = ran.choice(Z)
            # Set the value of Zi in x by sampling from P(Zi|mb(Zi))
            sample_key, sample_value, sample_value_index = self.sample(Z_k)
            x.append(self.getState(Z_k, sample_key))
            
            
            # break down P() with bayes rule to use the floats
            # C[j] <- C[j] + 1 where xj is the value of X in x
        return self.norm(C) # Normalize C
        