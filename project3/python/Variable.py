


class Variable:
    def __init__(self, name, type, numTypes, types):
        self.name = name
        self.type = type
        self.numTypes = numTypes
        self.types = types
        self.marginal = None
        self.parentList = []
        self.childList = []
        self.probabilityTables = []
    
    # def __eq__(self, other):
    #     return self.name == other.name         

    def setMarginal(self, margList):
        self.marginal = margList

    def appendParent(self, parentVar):
        self.parentList.append(parentVar)

    def appendChild(self, childVar):
        self.childList.append(childVar)

    def appendProbTable(self, probabilities):
        self.probabilityTables.append(probabilities)
        
    def transformProbTable(self):
        newTables = dict()
        for probTable in self.probabilityTables:
            var_names = []
            var_values = []
            for value in probTable:
                try:
                    value = float(value)
                    var_values.append(value)
                except ValueError:
                    var_names.append(value)
            newTables[tuple(var_names)] = var_values
            # newTables.append(newTable)

    def rootVariableCheck(self):
        return len(self.parentList) == 0

    def leafVariableCheck(self):
        return len(self.childList) == 0

    def getProbTable(self):
        self.probabilityTables = self.transformProbTable()
        return self.probabilityTables

    def getParents(self):
        return self.parentList

    def getChildren(self):
        return self.childList

    def getVarName(self):
        return self.name

    def getVarType(self):
        return self.type

    def getVarNumTypes(self):
        return self.numTypes

    def getVarTypes(self):
        return self.types
    
    def getMarginal(self):
        return self.marginal
