

class MarkovNode():
    
    def __init__(self, state: str, i: int, j: int) -> None:
        self.state = state
        self.i = i
        self.j = j
        self.utility = 0
        self.best_move = None
        self.neighbors = list()
    
    def get_state(self):
        return self.state

    def get_wall_state(self) -> bool:
        return self.get_state() == "wall"
    
    def get_finish_state(self) -> bool:
        return self.get_state() == "finish"

    def check_and_set_utility(self) -> None:
        if self.get_wall_state():
            self.utility = -1
        if self.get_finish_state():
            self.utility = 1
    
    def set_utility(self, value: float) -> None:
        self.utility = value
    
    def set_wall_utility(self) -> None:
        self.utility = -1
    
    def set_finish_utility(self) -> None:
        self.utility = 1
    
    