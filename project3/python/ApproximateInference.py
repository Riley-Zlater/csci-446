import random as ran


def markov_blanket(variable: object) -> list:
    markov_list = list()

    #if not variable.rootVariableCheck():  # if the variable has parents
    for parent in variable.getParents():  
        markov_list.append(parent)  # add the parents to the markov_list
        
    if not variable.leafVariableCheck():  # if the variable has children
        for child in variable.getChildren():  
            markov_list.append(child)  # add the children to the markov_list
            if child.getParents():  # if the children of the variable have parents
                for child_par in child.getParents():
                    if child_par != variable:  # if the parent of the child is not the variable
                        markov_list.append(child_par)  # add the childs parents to the markov_list

    return markov_list

def sample(variable: object, evidence: dict, markov_blanket: list) -> None:
    if variable.rootVariableCheck():  # variable is a root already know marginal
        return
    else:
        variable.setCurrentType(ran.choice(variable.getVarTypes()))  # set the type of the random variable

        for var in markov_blanket:
            var.setCurrentType(ran.choice(var.getVarTypes()))  # set the types for the vars in markov blanket

        key = list()
        for var in variable.getParents():
            key.append(var.getCurrentType())  # make key tuple
        key = tuple(key)

        for keys, value in variable.getProbTable().items():
            if key == keys:
                variable.setMarginal(value)


        #variable.setMarginal(variable.getProbTable()[key])  # use key tuple to get the correct values for the variable

    return

def gibbs_sampling(evidence: dict, bayes_net: list, num_iter: int) -> None:

    if evidence:  # if there is evidence
            for var_name, var_type in evidence.items():  # loop through the evidence
                for var in bayes_net:  # loop through the bayes_net
                    if var_name == var.getVarName():  # if the key of the evidence is the same name as a variable in the bayes_net
                        var.setCurrentType(var_type)  # set the current type of that variable

    for i in range(num_iter):
        Z_i = ran.choice(bayes_net)
        mbZ_i = markov_blanket(Z_i)
        sample(Z_i, evidence, mbZ_i)
        
    return