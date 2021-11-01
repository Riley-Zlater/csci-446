from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("../inputFiles/alarm.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_make_factor():
    
    return

def test_order():
    
    ordered_variables = exact_inference.order(variables)

    if len(ordered_variables) != len(variables):
        print("lengths are not equal! " +
            str(len(ordered_variables))+ " " + str(len(variables)))
        return False

    for o_var in ordered_variables:
        if exact_inference.check_list(o_var, variables) == False:
            return False
    
    return True


print(test_order())