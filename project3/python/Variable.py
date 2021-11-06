


class Variable:
    def __init__(self, name: str, type: tuple, numTypes: int, types: list) -> None:
        self.name = name
        self.type = type
        self.numTypes = numTypes
        self.types = types
        self.marginal = list()
        self.parentList = list()
        self.childList = list()
        self.probabilityTables = dict()
        self.current_type = str()

    def setCurrentType(self, type) -> None:
        self.current_type = type
    
    def setMarginal(self, margList: list) -> None:
        self.marginal = margList

    def appendParent(self, parentVar: object) -> None:
        self.parentList.append(parentVar)

    def appendChild(self, childVar: object) -> None:
        self.childList.append(childVar)

    def setProbTable(self, probabilities: dict) -> None:
        self.probabilityTables = probabilities

    def rootVariableCheck(self) -> bool:
        return len(self.parentList) == 0

    def leafVariableCheck(self) -> bool:
        return len(self.childList) == 0

    def getProbTable(self) -> dict:
        return self.probabilityTables

    def getParents(self) -> list:
        return self.parentList

    def getChildren(self) -> list:
        return self.childList

    def getVarTypes(self) -> list:
        return self.types
    
    def getMarginal(self) -> list:
        return self.marginal

    def getVarName(self) -> str:
        return self.name

    def getCurrentType(self) -> str:
        return self.current_type

    def getVarType(self) -> str:
        return self.type

    def getVarNumTypes(self) -> int:
        return self.numTypes

