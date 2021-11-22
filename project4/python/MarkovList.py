

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

    def insert_list(self, sub_list: list) -> None:
        self.markov_list.append(sub_list)
    
    def display_markov_list(self) -> None:
        for line in self.markov_list:
            markov_line = list()
            for node in line:
                markov_line.append(node.state)
            print(markov_line)
    
    def get_node(self, i: int, j: int) -> MarkovNode:
        return self.markov_list[i][j]
