from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ApproximateInference import ApproximateInference as AI

with open("C:/Users/riley/repos/csci-446/project3/inputFiles/alarm.bif", "r") as file:
#with open("../inputFiles/alarm.bif", "r") as file:
    rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)

for var in variables:
    if var.getVarName() == "HYPOVOLEMIA":
        local_var = var
        break

approx = AI()
base_e = {}
alarm_little_e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH"}
alarm_moderate_e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH",
                    "HRSAT": "LOW", "HREKG": "LOW", "HISTORY": "TRUE"}

approx.gibbs_sampling(alarm_moderate_e, variables, 10000)

for var in variables:
    print(var.getVarName(), var.getMarginal())
