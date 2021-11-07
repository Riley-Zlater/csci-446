from ParseInput import ParseInputBIF
from ParseInput import displayVariables
from ExactInference import ExactInference

with open("project3/inputFiles/child.bif", "r") as file:
        rawBIF = file.readlines()

variables = ParseInputBIF(rawBIF)
exact_inference = ExactInference()

def test_make_factor():
    print(variables[-1].getVarName())
    a, b = exact_inference.make_factor(variables[-1], {})
    # print(a.index('BP'))
    try:
        print(a.index('CUNT'))
    except:
        ValueError
    return a, b

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

    for var in variables:
        if var.getVarName() == 'VENTALV':
            ventalv = var
        if var.getVarName() == 'PVSAT':
            pvsat = var
        

    a, b = exact_inference.make_factor(ventalv, {})
    c, d = exact_inference.make_factor(pvsat, {})
    factor =    {a: b,
                 c: d}


    exact_inference.sum_out('VENTALV', factor, variables)

def test_sum_out_simple():
    bp = None

    for var in variables:
        if var.getVarName() == 'BP':
            bp = var
        

    a, b = exact_inference.make_factor(bp, {})
    factor =    {a: b}


    exact_inference.sum_out('BP', factor, variables)

def test_sum_out_book():
    f1 = {("X", "Y"): 
            { 
                ('T', 'T'): 0.3,
                ('T', 'F'): 0.7,
                ('F', 'T'): 0.9,
                ('F', 'F'): 0.1   
            },
          ("Y", "Z"): 
            { 
                ('T', 'T'): 0.2,
                ('T', 'F'): 0.8,
                ('F', 'T'): 0.6,
                ('F', 'F'): 0.4   
            }
        }
    return exact_inference.sum_out('X', f1, variables)

def test_pointwise_product():
    ventalv = None
    pvsat = None

    for var in variables:
        if var.getVarName() == 'VENTALV':
            ventalv = var
        if var.getVarName() == 'PVSAT':
            pvsat = var
        

    a, b = exact_inference.make_factor(ventalv, {})
    c, d = exact_inference.make_factor(pvsat, {})
    factor =    {a: b,
                 c: d}

    
    ans = exact_inference.pointwise_product(factor, variables)
    return ans

def test_pointwise_product_book_ex():
    f1 = {("X", "Y"): 
            { 
                ('T', 'T'): 0.3,
                ('T', 'F'): 0.7,
                ('F', 'T'): 0.9,
                ('F', 'F'): 0.1   
            },
          ("Y", "Z"): 
            { 
                ('T', 'T'): 0.2,
                ('T', 'F'): 0.8,
                ('F', 'T'): 0.6,
                ('F', 'F'): 0.4   
            }
        }

    
    ans = exact_inference.pointwise_product(f1, variables)
    return ans

def test_exact_inference():
    ventalv = None

    for var in variables:
        if var.getVarName() == 'Disease':
            ventalv = var
    
    ans = exact_inference.elimination_ask(ventalv, {"LowerBodyO2": "<5", "RUQO2": "12+", "CO2Report": ">=7.5",
                        "XrayReport": "Asy/Patchy"}, variables)
    return ans

print(test_exact_inference())