

class MarkovNode():
    
    def __init__(self, state: str, i: int, j: int) -> None:
        self.state = state
        self.i = i
        self.j = j
        self.utility = 0
    