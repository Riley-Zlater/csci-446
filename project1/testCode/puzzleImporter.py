# File name format: "Easy-P1.csv", "Med-P1.csv", "Hard-P1.csv", "Evil-P1.csv"

import numpy as np
import csv

def importPuzzle(file):
    rawPuzzle = np.array(list(csv.reader(open(file, "r"))))

    numRows, numCols = rawPuzzle.shape

    for j in range(numCols):
        for i in range(numRows):
            if len(rawPuzzle[i, j]) == 4:
                rawPuzzle[i, j] = rawPuzzle[i, j][3:]

            if rawPuzzle[i, j] == '?':
                rawPuzzle[i, j] = 0

    return rawPuzzle.astype(np.int)
