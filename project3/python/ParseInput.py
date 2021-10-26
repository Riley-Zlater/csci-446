

with open("../inputFiles/alarm.bif", "r") as file:
    rawBIF = file.readlines()




def ParseInputBIF(inputBIF):
    
    index = 0
    varList = []

    while index < len(inputBIF):
        line = inputBIF[index].split()
        
        if line[0] == "variable":
            varName = line[1]
            index += 1
            nextLine = inputBIF[index].split()
            varType = nextLine[1]
            numTypes = int(nextLine[3])
            varTypes = [type.replace(",", "") for type in nextLine[6:6+numTypes]]
            
            # make a new variable object with the arguements:
            # varName, varType, numTypes, varTypes
            # this mght help lmk what you think 
            # i know it's not even close to the design doc 
            # but I think it will make the project easier
            print("variable name:",varName,"\nvariable type:", varType,
            "\nnumber of types:", numTypes,"\ntypes:", varTypes,"\n")

            # append new variable object to varList

        if line[0] == "probability":
            line = inputBIF[index].split()

            # for variable in 
            pass

        index += 1



    


ParseInputBIF(rawBIF)
