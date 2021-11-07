import random as ran

class ApproximateInference():
    def __init__(self):
        pass

    def markov_blanket(self, variable: object) -> list:
        markov_list = list()

        if not variable.rootVariableCheck():
            for parent in variable.getParents():
                markov_list.append(parent)
        
        if not variable.leafVariableCheck():
            for child in variable.getChildren():
                markov_list.append(child)
                if child.getParents():
                    for child_par in child.getParents():
                        if child_par != variable:
                            markov_list.append(child_par)

        return markov_list

    def sample(self, variable: object, evidence: dict, markov_blanket: list, bayes_net: list) -> None:
        if variable.rootVariableCheck():  # variable already has prob
            return
        else:
            if evidence:  # set the evidence types
                for var_name, var_type in evidence.items():
                    for var in bayes_net:
                        if var_name == var.getVarName():
                            var.setCurrentType(var_type)

            if not variable.getCurrentType():
                variable.setCurrentType(ran.choice(variable.getVarTypes()))  # set the type of the random variable

            for var in markov_blanket:
                if not var.getCurrentType():
                    var.setCurrentType(ran.choice(var.getVarTypes()))  # set the types for the vars in markov blanket

            key = list()
            for var in variable.getParents():
                key.append(var.getCurrentType())  # make key tuple
            key = tuple(key)

            variable.setMarginal(variable.getProbTable()[key])  # use key tuple to get the correct values for the variable

        return

    def gibbs_sampling(self, evidence: dict, bayes_net: list, num_iter: int) -> None:

        for i in range(num_iter):
            Z_i = ran.choice(bayes_net)
            mbZ_i = self.markov_blanket(Z_i)
            self.sample(Z_i, evidence, mbZ_i, bayes_net)
        
        return