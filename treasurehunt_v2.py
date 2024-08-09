def treasure_hunt(matrix: list):
    # find starting & treasure cell
    def find_cell(letter: str):
        fcell = None
        rowindex = 0
        while fcell is None:
            if letter in matrix[rowindex]:
                fcell = (rowindex, matrix[rowindex].index(letter))
            rowindex += 1
        return fcell

    currentcells = [find_cell('S')]
    treasure = find_cell('T')

    triedcells = set()
    stepcounter = 0
    # find shortest path
    while treasure not in currentcells:
        newcells = []
        # search for cells to go
        for cell in currentcells:
            nextcells = [(cell[0] + 1, cell[1]),
                         (cell[0] - 1, cell[1]),
                         (cell[0], cell[1] + 1),
                         (cell[0], cell[1] - 1)]
            # check if cells are accessible
            for coordinates in nextcells:
                if coordinates not in triedcells:
                    in_matrix = (-1 not in coordinates) and (coordinates[0] < len(matrix)) and (coordinates[1] < len(matrix[0]))
                    if in_matrix and matrix[coordinates[0]][coordinates[1]] != '#':
                        newcells.append(coordinates)
                # avoiding repetition
                triedcells.add(coordinates)

        currentcells = newcells

        if len(currentcells) == 0:
            return -1

        stepcounter += 1
    return stepcounter

grid = [
    ['-', '-', '-', '#', '-', '-', '-', '-'],
    ['#', '#', '-', '#', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-', '#', '-', '-'],
    ['-', '#', '#', '#', '-', '-', 'T', '-'],
    ['-', '-', 'S', '#', '-', '#', '-', '-']
]

print(treasure_hunt(grid))
