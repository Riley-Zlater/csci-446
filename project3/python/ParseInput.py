import Variable

def topo_sort(variables: list) -> list:
    """This function topologically sorts the data."""
    sorted_data = list()
    temp_set = list()

    for variable in variables:
        if variable.rootVariableCheck():
            temp_set.append(variable)
    
    while temp_set:
        var = temp_set.pop(0)
        sorted_data.append(var)

        for child in var.getChildren():
            if all([parent in sorted_data for parent in child.getParents()]):
                temp_set.append(child)
    
    return sorted_data

def ParseInputBIF(inputBIF: list) -> list:
    """This function parses the input BIF file into Variable objects."""
    index = 0
    varList = []

    while index < len(inputBIF):
        line = inputBIF[index].split()
        
        if line[0] == "variable":
            varName = line[1]
            nextIndex = index + 1
            nextLine = inputBIF[nextIndex].split()
            varType = nextLine[1]
            numTypes = int(nextLine[3])
            varTypesList = [type.replace(",", "") for type in nextLine[6:6+numTypes]]
            varList.append(Variable.Variable(varName, varType, numTypes, varTypesList))

        elif line[0] == "probability":
            for variable in varList:
                if variable.getVarName() == line[2]:
                    tempVar = variable
                    break
                
            if line[3] == "|":
                tempIndex = 4
                while line[tempIndex] != ")":
                    for variable in varList:
                        if variable.getVarName() == line[tempIndex].strip(","):
                            tempVar.appendParent(variable)
                            variable.appendChild(tempVar)
                            break
                    tempIndex += 1
            
        if "table" == line[0]:
            del line[0]
            line = [value.replace(",", "") for value in line]
            line = [value.replace(";", "") for value in line]
            tempVar.setMarginal([float(prob) for prob in line])

        if line[0][0] == "(":
            prob_table = dict()
            while inputBIF[index][0] != "}":
                line = inputBIF[index].split()
                keys = list()
                values = list()
                line = [value.replace(",", "") for value in line]
                line = [value.replace(";", "") for value in line]
                line = [value.replace(")", "") for value in line]
                line = [value.replace("(", "") for value in line]
                for element in line:
                    try:
                        values.append(float(element))
                    except ValueError:
                        keys.append(element)
                        continue
                prob_table[tuple(keys)] = values
                index += 1
            tempVar.setProbTable(prob_table)
        index += 1
    return topo_sort(varList)

def displayVariables(varList: list) -> None:
    """This function will display the data."""
    for var in varList:
        print("\nVariable Name:", var.getVarName())
        print("\nType:", var.getVarTypes())
        print("\nParents:")    
        for p in var.getParents():
            print(p.getVarName())
        print("\nChildren: ")
        for c in var.getChildren():
            print(c.getVarName())
        if var.getMarginal():
            print("\nMarginal:")
            print(var.getMarginal())
        else:
            print("\nProb Table:")
            for key, value in var.getProbTable().items():
                print(f"Key: {str(key):25}Value: {value}")
        print()
        print()
