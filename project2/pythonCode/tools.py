
from GameBoard import Cell

def test_edge(cell, boardSize, direction):
    i, j = cell.getIndex()
    if direction == "north" and i - 1 == 0:
        return True
    if direction == "east" and j - 1 == 0:
        return True
    if direction == "south" and i + 1 > boardSize:
        return True
    if direction == "west" and j + 1 > boardSize:
        return True
