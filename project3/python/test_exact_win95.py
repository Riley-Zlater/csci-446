from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("../inputFiles/win95pts.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_exact_inference():
    for var in variables:
        if var.getVarName() == 'Problem1':
            p1 = var
        if var.getVarName() == 'Problem2':
            p2 = var
        if var.getVarName() == 'Problem3':
            p3 = var
        if var.getVarName() == 'Problem4':
            p4 = var
        if var.getVarName() == 'Problem5':
            p5 = var
        if var.getVarName() == 'Problem6':
            p6 = var


    # No Evidence
    base_e = {}
    # Alarm Evidence
    win95pts_e1 = {"Problem1": "No_Output"}
    win95pts_e2 = {"Problem2": "Too_Long"}
    win95pts_e3 = {"Problem3": "No"}
    win95pts_e4 = {"Problem4": "No"}
    win95pts_e5 = {"Problem5": "No"}
    win95pts_e6 = {"Problem6": "Yes"}

    search = [p1, p2, p3, p4, p5, p6]
    ev_level = [win95pts_e6, win95pts_e5, win95pts_e4, win95pts_e3, win95pts_e2, win95pts_e1, base_e]

    for ev in ev_level:
        for item in search:
            print(str(item.getVarName()) + " " + str(ev))
            print(exact_inference.elimination_ask(item, ev, variables))
    
    ##----- End Alarm -----##

# print(test_exact_inference())
test_exact_inference()