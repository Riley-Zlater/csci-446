

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

    def insert_list(self, sub_list: list()) -> None:
        self.markov_list.append(sub_list)
    
    def display_markov_list(self) -> None:
        for line in self.markov_list:
            bitcher = list()
            for node in line:
                bitcher.append(node.state)
            print(bitcher)
    
    def display_markov_contents(self) -> None:
        for i, row in enumerate(self.markov_list):
            for j, node in enumerate(row):
                if node.state != "wall":
                    print(f"Node at position {i}, {j}")
                    print(f"State = {node.state}")
                    print(f"Index = {node.i}, {node.j}")
                    print(f"Utility = {node.utility}")
                    print(f"Best Move = {node.best_move}")
                    print(f"Neighbors = {node.neighbors}")
                    print()

    def get_node(self, i: int, j: int) -> MarkovNode:
        return self.markov_list[i][j]
