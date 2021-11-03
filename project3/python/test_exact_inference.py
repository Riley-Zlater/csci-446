from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("../inputFiles/alarm.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_make_factor():
    print(variables[-1].getVarName())
    a, b = exact_inference.make_factor(variables[-1], {})
    print(a.index('BP'))
    try:
        print(a.index('CUNT'))
    except:
        ValueError
    return a, b

# print(test_make_factor())

def test_order():
    
    ordered_variables = exact_inference.order(variables)

    if len(ordered_variables) != len(variables):
        print("lengths are not equal! " +
            str(len(ordered_variables))+ " " + str(len(variables)))
        return False

    for o_var in ordered_variables:
        if exact_inference.check_list(o_var, variables) == False:
            return False
    
    return True

def test_sum_out():
    ventalv = None
    pvsat = None
    minvol = None

    for var in variables:
        if var.getVarName() == 'VENTLUNG':
            ventalv = var
        if var.getVarName() == 'EXPCO2':
            pvsat = var
        if var.getVarName() == 'MINVOL':
            minvol = var

    a, b = exact_inference.make_factor(ventalv, {})
    c, d = exact_inference.make_factor(pvsat, {})
    e, f = exact_inference.make_factor(minvol, {})
    factor =    {a: b,
                 c: d,
                 e: f}


    exact_inference.sum_out('VENTLUNG', factor, variables)
# print(test_order())

test_sum_out()