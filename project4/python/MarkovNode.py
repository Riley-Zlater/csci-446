

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
        self.possible_actions =     [(0, 0),   (0, 1),  (0, -1), 
                                     (1, 1),   (1, 0),  (-1, 0), 
                                     (-1, -1), (-1, 1), (1, -1)]
        # self.prune_poss_actions()
        self.acceleration = dict()

    def get_acceleration(self):
        return (self.x_acceleration, self.y_acceleration)

    def get_condition(self):
        return self.condition

    def get_wall_condition(self) -> bool:
        return self.condition == "#"
    
    def get_finish_condition(self) -> bool:
        return self.condition == "F"
    
    def get_position(self) -> tuple:
        return (self.x_pos, self.y_pos)
    
    def get_velocity(self) -> tuple:
        return (self.x_velocity, self.y_velocity)
    
    def get_possible_actions(self) -> list:
        return self.possible_actions
    
    def get_best_move_indices(self) -> list:
        return self.best_move.get_position()
    
    def get_best_acceleration(self, velocity) -> tuple:
        return self.acceleration[velocity]
 
    def check_and_set_utility(self) -> None:
        if self.get_wall_condition():
            self.utility = -1.0
        if self.get_finish_condition():
            self.utility = 1.0
    
    def prune_poss_actions(self) -> None:
        for action in self.possible_actions:
            x_acc, y_acc = action
            if -5 >= self.x_velocity + x_acc or self.x_velocity + x_acc >= 5 or -5 >= self.y_velocity + y_acc or self.y_velocity + y_acc >= 5:
                self.possible_actions.remove(action)
    
    def set_condition(self, condition: str) -> None:
        self.condition = condition

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
    
    def add_acceleration(self, velocity: tuple, acceleration: tuple) -> None:
        self.acceleration[velocity] = acceleration
    
    def set_velocity(self, velocity: tuple) -> None:
        input_x_velocity, input_y_velocity = velocity
        if input_x_velocity <= -5:
            input_x_velocity = -5
        if input_x_velocity >= 5:
            input_x_velocity = 5
        if input_y_velocity <= -5:
            input_y_velocity = -5
        if input_y_velocity >= 5:
            input_y_velocity = 5
        
        self.x_velocity = input_x_velocity
        self.y_velocity = input_y_velocity
        