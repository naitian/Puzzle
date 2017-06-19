
def validate(puzzle):
    """

    :puzzle: TODO
    :returns: TODO

    """
    pieces = []
    for i in range(len(puzzle) // 4):
        pieces.append(puzzle[i:i + 4])
    print(pieces)
