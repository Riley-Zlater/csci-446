from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

def test_make_input():
    return

def test_order():
    with open("../inputFiles/alarm.bif", "r") as file:
        rawBIF = file.readlines()

    variables = ParseInputBIF(rawBIF)
    exact_inference = ExactInference()
    ordered_variables = exact_inference.order(variables)

    if len(ordered_variables) != len(variables):
        print("lengths are not equal! " +
            str(len(ordered_variables))+ " " + str(len(variables)))
        # displayVariables(ordered_variables)
        # print("variables\n")
        # displayVariables(variables)
        return False

    for o_var in ordered_variables:
        print(o_var)
    
    return True


print(test_order())