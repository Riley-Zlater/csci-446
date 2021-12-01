

from MarkovNode import MarkovNode


class MarkovList():

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.markov_list = list()

    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    
    def get_markov_list(self) -> list:
        return self.markov_list

    def insert_list(self, sub_list: list) -> None:
        self.markov_list.append(sub_list)
    
    def get_markov_node(self, node: MarkovNode) -> MarkovNode:
        return self.get_node(node.x_pos, node.y_pos)
    
    def get_markov_utilities(self) -> list:
        U = list()
        for markov_line in self.markov_list:
            U_line = list()
            for markov_node in markov_line:
                markov_node.check_and_set_utility()
                U_line.append(markov_node.utility)
            U.append(U_line)
        return U
    
    def display_markov_list(self) -> None:
        for line in self.markov_list:
            markov_line = list()
            for node in line:
                markov_line.append(round(node.utility, 2))
            print(markov_line)
    
    def display_markov_list_best_move(self) -> None:
        for line in self.markov_list:
            markov_line = list()
            
            for node in line:
                if node.get_condition() in ['w', 'f']:
                    markov_line.append([0,0])
                else:
                    markov_line.append(node.get_best_move_indices())
            print(markov_line)
    
    def display_markov_list_velocity(self) -> None:
        for line in self.markov_list:
            markov_line = list()
            
            for node in line:
                if node.get_condition() in ['w', 'f']:
                    markov_line.append([0,0])
                else:
                    markov_line.append(node.get_velocity())
            print(markov_line)

    def display_markov_contents(self) -> None:
        for i, row in enumerate(self.markov_list):
            for j, node in enumerate(row):
                if node.condition != "w":
                    print(f"Node at position {i}, {j}")
                    print(f"Condition = {node.condition}")
                    print(f"Index = {node.x_pos}, {node.y_pos}")
                    print(f"Velocity = {node.x_velocity}, {node.y_velocity}")
                    print(f"Acceleration = {node.x_acceleration}, {node.y_acceleration}")
                    print(f"Utility = {node.utility}")
                    print(f"Best Move = {node.best_move}")
                    print()

    def get_node(self, i: int, j: int) -> MarkovNode:
        return self.markov_list[i][j]
