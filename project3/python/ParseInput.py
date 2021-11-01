
import Variable


def ParseInputBIF(inputBIF):
    
    index = 0
    varList = []

    # begin file
    while index < len(inputBIF):
        line = inputBIF[index].split()
        
        # find first variable
        if line[0] == "variable":
            # variable name
            varName = line[1]
            # move to the next line
            index += 1
            nextLine = inputBIF[index].split()
            # variable type 
            varType = nextLine[1]
            # number of types
            numTypes = int(nextLine[3])
            # list of types
            varTypesList = tuple([type.replace(",", "") for type in nextLine[6:6+numTypes]])
            # create object to store the new variable
            varList.append(Variable.Variable(varName, varType, numTypes, varTypesList))

        # find the first probability
        
        elif line[0] == "probability":
            
            line = inputBIF[index].split()

            # check in the list of variable objects for the name
            # store in tempVar
            for variable in varList:
                if variable.getVarName() == line[2]:
                    tempVar = variable
                    break
                
            # look at the "given" part of the probability
            if line[3] == "|":
                tempIndex = 4
                while line[tempIndex] != ")":
                    for variable in varList:
                        if variable.getVarName() == line[tempIndex].strip(","):
                            tempVar.appendParent([variable])
                            variable.appendChild([tempVar])
                            break
                    tempIndex += 1
            index += 1
            
                
        probMatrix = []
        probTable = []
        line = inputBIF[index].split()
            
        if "table" == line[0]:
            del line[0]

            line = [value.replace(",", "") for value in line]
            probabilities = [value.replace(";", "") for value in line]

            probTable = [float(prob) for prob in probabilities]

            tempVar.setMarginal(probTable)

        if line[0][0] == "(":

            line = [value.replace(",", "") for value in line]
            line = [value.replace(";", "") for value in line]
            line = [value.replace(")", "") for value in line]
            line = [value.replace("(", "") for value in line]

            for i in range(len(line)):
                try:
                    line[i] = float(line[i])
                except ValueError:
                    continue
                
            probMatrix = line
            tempVar.appendProbTable(probMatrix)
        
        index += 1
    return varList


def displayVariables(varList):
    for var in varList:
        print("\nvariable name:",var.getVarName())
        print("\ntype:", var.getVarTypes())
        print("\nParents:")    
        for parVar in var.getParents():
            for p in parVar:
                print(p.getVarName())
        print("\nchildren: ")
        for chiVar in var.getChildren():
            for c in chiVar:
                print(c.getVarName())
        if var.getMarginal() != None:
            print("\nMarginal:")
            print(var.getMarginal())
        else:
            print("\nprob table:")
            print(var.getProbTable())
        print()
        print()

# with open("C://Users/Riley/repos/csci-446/project3/inputFiles/alarm.bif", "r") as file:
# with open("/Users/cooperstrahan/School/csci-446/project3/inputFiles/child.bif", "r") as file:
#     rawBIF = file.readlines()

# variables = ParseInputBIF(rawBIF)

# displayVariables(variables)
