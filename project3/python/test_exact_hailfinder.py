from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("../inputFiles/hailfinder.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_exact_inference():
    for var in variables:
        if var.getVarName() == 'SatContMoist':
            satcont = var
        if var.getVarName() == 'LLIW':
            lliw = var

    # No Evidence
    base_e = {}
    # Alarm Evidence
    hailfinder_little_e = {"RSFcst": "XNIL", "N32StarFcst": "XNIL", "MountainFcst": "XNIL",
                            "AreaMoDryAir": "VeryWet"}
    hailfinder_moderate_e = {"RSFcst": "XNIL", "N32StarFcst": "XNIL", "MountainFcst": "XNIL",
                            "AreaMoDryAir": "VeryWet", "CombVerMo": "Down", "AreaMeso_ALS": "Down",
                            "CurPropConv": "Strong"}

    search = [satcont, lliw]
    ev_level = [hailfinder_moderate_e, hailfinder_little_e, base_e]

    for ev in ev_level:
        for item in search:
            print(str(item.getVarName()) + " " + str(ev))
            print(exact_inference.elimination_ask(item, ev, variables))
    
    ##----- End Alarm -----##

# print(test_exact_inference())
test_exact_inference()