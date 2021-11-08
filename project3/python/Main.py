# Written by Riley Slater and Cooper Strahan
from ParseInput import ParseInputBIF, displayVariables
from ResultsApprox import test_approx


"""Run this file to do the Gibbs Sampling testing"""


with open("C:/Users/riley/repos/csci-446/project3/inputFiles/win95pts.bif", "r") as file:
# with open("../inputFiles/win95pts.bif", "r") as file:
    win95pts_bif = file.readlines()
with open("C:/Users/riley/repos/csci-446/project3/inputFiles/insurance.bif", "r") as file:
# with open("../inputFiles/insurance.bif", "r") as file:
    insurance_bif = file.readlines()
with open("C:/Users/riley/repos/csci-446/project3/inputFiles/hailfinder.bif", "r") as file:
# with open("../inputFiles/hailfinder.bif", "r") as file:
    hailfinder_bif = file.readlines()
with open("C:/Users/riley/repos/csci-446/project3/inputFiles/child.bif", "r") as file:
# with open("../inputFiles/child.bif", "r") as file:
    child_bif = file.readlines()
with open("C:/Users/riley/repos/csci-446/project3/inputFiles/alarm.bif", "r") as file:
# with open("../inputFiles/alarm.bif", "r") as file:
    alarm_bif = file.readlines()

alarm_variables = ParseInputBIF(alarm_bif)
child_varaibles = ParseInputBIF(child_bif)
hailfinder_variables = ParseInputBIF(hailfinder_bif)
insurance_variables = ParseInputBIF(insurance_bif)
win95pts_variables = ParseInputBIF(win95pts_bif)

test_approx(alarm_variables, child_varaibles, hailfinder_variables, insurance_variables,
            win95pts_variables)




