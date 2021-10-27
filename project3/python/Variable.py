


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

    def setMarginal(self, margList):
        self.marginal = margList

    def appendParent(self, parentVar):
        self.parentList.append(parentVar)

    def appendChild(self, childVar):
        self.childList.append(childVar)

    def appendProbTable(self, probabilities):
        self.probabilityTables.append(probabilities)
        
    """
        if self.rootVariableCheck():
            self.marginal = []
            for prob in probabilities:
                index = 0
                while index < len(prob):
                    self.marginal.append(probabilities[index])
                    index += 1
    """
    def rootVariableCheck(self):
        return len(self.parentList) == 0

    def leafVariableCheck(self):
        return len(self.childList) == 0

    def getProbTable(self):
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
