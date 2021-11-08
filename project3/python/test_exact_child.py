from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("../inputFiles/child.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_exact_inference():
    for var in variables:
        if var.getVarName() == 'Disease':
            disease = var

    # No Evidence
    base_e = {}
    # Alarm Evidence
    child_little_e = {"LowerBodyO2": "<5", "RUQO2": "12+", "CO2Report": ">=7.5",
                        "XrayReport": "Asy/Patchy"}
    child_moderate_e = {"LowerBodyO2": "<5", "RUQO2": "12+", "CO2Report": ">=7.5",
                        "XrayReport": "Asy/Patchy", "GruntingReport": "Yes",
                        "LVHReport": "Yes", "Age": "11-30 Days"}

    search = [disease]
    ev_level = [base_e, child_little_e, child_moderate_e]

    for ev in ev_level:
        for item in search:
            print(str(item) + " " + str(ev))
            print(exact_inference.elimination_ask(item, ev, variables))
    
    ##----- End Alarm -----##

# print(test_exact_inference())
test_exact_inference()