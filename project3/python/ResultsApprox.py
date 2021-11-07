from ApproximateInference import gibbs_sampling

def test_approx(alarm_variables: object, child_variables: object,
                hailfinder_variables: object, insurance_variables: object, 
                win95pts_variables: object):

    test_alarm(alarm_variables)
    test_child(child_variables)
    test_hailfinder(hailfinder_variables)
    test_insurance(insurance_variables)
    test_win95pts(win95pts_variables)


def test_alarm(variables):
    # No Evidence
    base_e = {}
    # Alarm Evidence
    alarm_little_e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH"}
    alarm_moderate_e = {"HRBP": "HIGH", "CO": "LOW", "BP": "HIGH",
                        "HRSAT": "LOW", "HREKG": "LOW", "HISTORY": "TRUE"}

    gibbs_sampling(base_e, variables, 10000)
    alarm_list = ["HYPOVOLEMIA", "LVFAILURE", "ERRLOWOUTPUT"]
    print("Alarm Network No Evidence")
    for var in variables:
        if var.getVarName() in alarm_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(alarm_little_e, variables, 10000)
    print("Alarm Network Little Evidence")
    for var in variables:
        if var.getVarName() in alarm_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(alarm_moderate_e, variables, 10000)
    print("Alarm Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in alarm_list:
            print(var.getVarName(), var.getMarginal())
    print()
    ##----- End Alarm -----##

def test_child(variables):
    base_e = {}
    # Child Evidence
    child_little_e = {"LowerBodyO2": "<5", "RUQO2": "12+", "CO2Report": ">=7.5",
                        "XrayReport": "Asy/Patchy"}
    child_moderate_e = {"LowerBodyO2": "<5", "RUQO2": "12+", "CO2Report": ">=7.5",
                        "XrayReport": "Asy/Patchy", "GruntingReport": "Yes",
                        "LVHReport": "Yes", "Age": "11-30 Days"}
    child_list = ["Disease"]
    gibbs_sampling(base_e, variables, 10000)
    alarm_list = ["HYPOVOLEMIA", "LVFAILURE", "ERRLOWOUTPUT"]
    print("Child Network No Evidence")
    for var in variables:
        if var.getVarName() in child_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(child_little_e, variables, 10000)
    print("Child Network Little Evidence")
    for var in variables:
        if var.getVarName() in child_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(child_moderate_e, variables, 10000)
    print("Child Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in child_list:
            print(var.getVarName(), var.getMarginal())
    print()
    ##----- End Child -----##

def test_hailfinder(variables):
    base_e = {}
    # Hailfinder Evidence
    hailfinder_little_e = {"RSFcst": "XNIL", "N32StarFcst": "XNIL", "MountainFcst": "XNIL",
                            "AreaMoDryAir": "VeryWet"}
    hailfinder_moderate_e = {"RSFcst": "XNIL", "N32StarFcst": "XNIL", "MountainFcst": "XNIL",
                            "AreaMoDryAir": "VeryWet", "CombVerMo": "Down", "AreaMeso_ALS": "Down",
                            "CurPropConv": "Strong"}
    gibbs_sampling(base_e, variables, 10000)
    hailfinder_list = ["SatContMoist", "LLIW"]
    print("Hailfinder Network No Evidence")
    for var in variables:
        if var.getVarName() in hailfinder_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(hailfinder_little_e, variables, 10000)
    print("Hailfinder Network Little Evidence")
    for var in variables:
        if var.getVarName() in hailfinder_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(hailfinder_moderate_e, variables, 10000)
    print("Hailfinder Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in hailfinder_list:
            print(var.getVarName(), var.getMarginal())
    print()
    ##----- End Hailfinder -----##

def test_insurance(variables):
    base_e = {}
    # Insurance Evidence
    insurance_little_e = {"Age": "Adolescent", "GoodStudent": "False", "SeniorTrain": "False", "DrivQuality": "Poor"}
    insurance_moderate_e = {"Age": "Adolescent", "GoodStudent": "False", "SeniorTrain": "False", "DrivQuality": "Poor",
                            "MakeModel": "Luxury", "CarValue": "FiftyThousand", "DrivHistory": "Zero"}
    gibbs_sampling(base_e, variables, 10000)
    insurance_list = ["MedCost", "ILiCost", "PropCost"]
    print("Insurance Network No Evidence")
    for var in variables:
        if var.getVarName() in insurance_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(insurance_little_e, variables, 10000)
    print("Insurance Network Little Evidence")
    for var in variables:
        if var.getVarName() in insurance_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(insurance_moderate_e, variables, 10000)
    print("Insurance Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in insurance_list:
            print(var.getVarName(), var.getMarginal())
    print()
    ##----- End Insurance -----##

def test_win95pts(variables):
    base_e = {}
    # Win95pts Evidence
    win95pts_e1 = {"Problem1": "No_Output"}
    win95pts_e2 = {"Problem2": "Too_Long"}
    win95pts_e3 = {"Problem3": "No"}
    win95pts_e4 = {"Problem4": "No"}
    win95pts_e5 = {"Problem5": "No"}
    win95pts_e6 = {"Problem6": "Yes"}
    gibbs_sampling(base_e, variables, 10000)
    win95pts_list = ["Problem1", "Problem2", "Problem3", "Problem4", "Problem5", "Problem6"]
    print("Win95pts Network No Evidence")
    for var in variables:
        if var.getVarName() in win95pts_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(win95pts_e1, variables, 10000)
    print("Win95pts Network Little Evidence")
    for var in variables:
        if var.getVarName() in win95pts_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(win95pts_e2, variables, 10000)
    print("Win95pts Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in win95pts_list:
            print(var.getVarName(), var.getMarginal())
    print()

    gibbs_sampling(win95pts_e3, variables, 10000)
    print("Win95pts Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in win95pts_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(win95pts_e4, variables, 10000)
    print("Win95pts Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in win95pts_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(win95pts_e5, variables, 10000)
    print("Win95pts Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in win95pts_list:
            print(var.getVarName(), var.getMarginal())
    print()
    
    gibbs_sampling(win95pts_e6, variables, 10000)
    print("Win95pts Network Moderate Evidence")
    for var in variables:
        if var.getVarName() in win95pts_list:
            print(var.getVarName(), var.getMarginal())
    print()