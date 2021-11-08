# Written by Riley Slater
import random as ran

def markov_blanket(variable: object) -> list:
    """This function finds the markov blanket of a given variable."""
    markov_list = list()

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

def sample(variable: object, markov_blanket: list) -> None:
    """
    This function randomly chooses values for each variable in the bay net.
    Based on those values decide a variables probability.
    """
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
        return

def gibbs_sampling(evidence: dict, bayes_net: list, num_iter: int) -> None:
    """
    This function applies the evidence to the variables values, if given,
    and uses the sample function to, after a number of iterations, approximate
    all of the variables probabilities.
    """

    if evidence:  # if there is evidence
            for var_name, var_type in evidence.items():  # loop through the evidence
                for var in bayes_net:  # loop through the bayes_net
                    if var_name == var.getVarName():  # if the key of the evidence is the same name as a variable in the bayes_net
                        var.setCurrentType(var_type)  # set the current type of that variable

    for _ in range(num_iter):
        Z_i = ran.choice(bayes_net)
        mbZ_i = markov_blanket(Z_i)
        sample(Z_i, mbZ_i)  
    return