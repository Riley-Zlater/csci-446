

class MarkovNode():
    
    def __init__(self, state: str, i: int, j: int) -> None:
        self.condition = state
        self.x_pos = i
        self.y_pos = j
        self.x_velocity
        self.y_velocity
        self.x_acceleration
        self.y_acceleration
        self.utility = 0
        self.best_move = None
        self.action = [0,0]
    
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
    
