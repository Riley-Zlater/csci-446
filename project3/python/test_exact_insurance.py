from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("../inputFiles/insurance.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_exact_inference():
    for var in variables:
        if var.getVarName() == 'MedCost':
            medcost = var
        if var.getVarName() == 'ILiCost':
            ilicost = var
        if var.getVarName() == 'PropCost':
            propcost = var


    # No Evidence
    base_e = {}
    # Alarm Evidence
    insurance_little_e = {"Age": "Adolescent", "GoodStudent": "False", "SeniorTrain": "False", "DrivQuality": "Poor"}
    insurance_moderate_e = {"Age": "Adolescent", "GoodStudent": "False", "SeniorTrain": "False", "DrivQuality": "Poor",
                            "MakeModel": "Luxury", "CarValue": "FiftyThou", "DrivHistory": "Zero"}
   

    search = [medcost, ilicost, propcost]
    ev_level = [base_e, insurance_little_e, insurance_moderate_e]

    # exact_inference.elimination_ask(medcost, insurance_little_e, variables)
    # exact_inference.elimination_ask(medcost, insurance_moderate_e, variables)

    for ev in ev_level:
        for item in search:
            print(str(item.getVarName()) + " " + str(ev))
            print(exact_inference.elimination_ask(item, ev, variables))
    
    ##----- End Alarm -----##

# print(test_exact_inference())
test_exact_inference()