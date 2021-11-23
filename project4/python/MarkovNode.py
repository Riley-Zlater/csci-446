

class MarkovNode():
    
    def __init__(self, condition: str, i: int, j: int) -> None:
        self.condition = condition
        self.x_pos = i
        self.y_pos = j
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_acceleration = 0
        self.y_acceleration = 0
        self.utility = 0.0
        self.best_move = None
    
    def get_condition(self):
        return self.condition

    def get_wall_condition(self) -> bool:
        return self.condition == "w"
    
    def get_finish_condition(self) -> bool:
        return self.condition == "f"
    
    def get_position(self) -> tuple:
        return (self.x_pos, self.y_pos)
    
    def get_velocity(self) -> tuple:
        return (self.x_velocity, self.y_velocity)

    def check_and_set_utility(self) -> None:
        if self.get_wall_condition():
            self.utility = -1.0
        if self.get_finish_condition():
            self.utility = 1.0
    
    def set_utility(self, value: float) -> None:
        self.utility = value
    
    def set_wall_utility(self) -> None:
        self.utility = -1
    
    def set_finish_utility(self) -> None:
        self.utility = 1

    def set_best_move(self, node: object) -> None:
        self.best_move = node
    
    def set_acceleration(self, acceleration: tuple) -> None:
        self.x_acceleration, self.y_acceleration = acceleration
    
    def set_velocity(self, velocity: tuple) -> None:
        self.x_velocity, self.y_velocity = velocity