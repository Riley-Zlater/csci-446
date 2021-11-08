from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

# with open("C:/Users/riley/repos/csci-446/project3/inputFiles/child.bif", "r") as file:
with open("project3/inputFiles/child.bif", "r") as file:
    rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)


def test_exact_inference():
    variables = ParseInputBIF(rawBIF)
    for var in variables:
        if var.getVarName() == 'Disease':
            disease = var

    # No Evidence
    base_e = {}
    # Alarm Evidence
    child_little_e = {"LowerBodyO2": "<5", "RUQO2": "12+", "CO2Report": ">=7.5",
                        "XrayReport": "Asy/Patchy"}
    child_moderate_e = {"LowerBodyO2": "<5", "RUQO2": "12+", "CO2Report": ">=7.5",
                        "XrayReport": "Asy/Patchy", "GruntingReport": "yes",
                        "LVHReport": "yes", "Age": "11-30_days"}

    search = [disease]
    ev_level = [child_moderate_e, child_little_e, base_e]

    for ev in ev_level:
        for item in search:
            variables = ParseInputBIF(rawBIF)
            exact_inference = ExactInference()
            print(str(item.getVarName()) + " " + str(ev))
            print(exact_inference.elimination_ask(item, ev, variables))
    
    # print(exact_inference.elimination_ask(disease, child_moderate_e, variables))

    ##----- End Alarm -----##

# print(test_exact_inference())
test_exact_inference()