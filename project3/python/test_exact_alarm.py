from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("../inputFiles/alarm.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_exact_inference():
    for var in variables:
        if var.getVarName() == 'HYPOVOLEMIA':
            hypo = var
        if var.getVarName() == 'LVFAILURE':
            lvfail = var
        if var.getVarName() == 'ERRLOWOUTPUT':
            errlow = var

    alarm_list = ["HYPOVOLEMIA", "LVFAILURE", "ERRLOWOUTPUT"]

    # No Evidence
    base_e = {}
    # Alarm Evidence
    alarm_little_e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH"}
    alarm_moderate_e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH",
                        "HRSAT": "LOW", "HREKG": "LOW", "HISTORY": "TRUE"}

    search = [hypo, lvfail, errlow]
    ev_level = [base_e, alarm_little_e, alarm_moderate_e]

    for ev in ev_level:
        for item in search:
            print(str(item) + " " + str(ev))
            print(exact_inference.elimination_ask(item, ev, variables))
    
    ##----- End Alarm -----##

# print(test_exact_inference())
test_exact_inference()