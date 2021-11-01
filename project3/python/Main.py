from ParseInput import ParseInputBIF
from ParseInput import displayVariables

with open("C:/Users/riley/repos/csci-446/project3/inputFiles/alarm.bif", "r") as file:
# with open("../inputFiles/child.bif", "r") as file:
    rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)

displayVariables(variables)