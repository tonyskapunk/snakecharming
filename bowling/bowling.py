# -*- coding: utf-8 -*-


def sushi(roll):
    """Transform a frame to a type, value structure
    Examples:
     - ['X', '-'] -> {type: "strike", values: [10, 0]}
     - ['2', '7'] -> {type: "regular", values: [2, 7]}
     - ['-', '-'] -> {type: "regular", values: [0, 0]}
     - ['1', '/'] -> {type: "spare", values: [1, 9]} 
     - ...         --    Any frame with 3 rolls is last:
     - ['X', 'X', 'X'] -> { type: "last", values: [10, 10, 10]}
     - ['X', '2', '/'] -> { type: "last", values: [10, 2, 8]}
     - ['X', '-', '-'] -> { type: "last", values: [10, 0, 0]}
    """
    sushi_roll = {}
    wasabi = []
    if len(roll) == 3:
        sushi_roll["type"] = "last"
    elif roll[0] == "X":
        sushi_roll["type"] = "strike"
    elif roll[1] == "/":
        sushi_roll["type"] = "spare"
    else:
        sushi_roll["type"] = "regular"

    for i in range(0, len(roll)):
        if roll[i] == "X":
            wasabi.append(10)
        elif roll[i] == "/":
            wasabi.append(10 - int(roll[i - 1]))
        elif roll[i] == "-":
            wasabi.append(0)
        else:
            wasabi.append(int(roll[i]))

    sushi_roll["values"] = wasabi
    return sushi_roll


def score(rolls):
    """ Do blowing math"""
    sushi_rolls = []

    # Do rolls
    for i in range(0, len(rolls)):
        sushi_rolls.append(sushi(rolls[i]))

    # Do blowing math
    dimsum = 0
    for i, roll in enumerate(sushi_rolls):
        (t, v) = roll.values()

        # Strikes
        if t == "strike":
            # Get next frame
            (nt, nv) = sushi_rolls[int(i + 1)].values()
            dimsum += sum(v) + sum(nv[0:2])

            # Also, if the nt is strike count the following
            if nt == "strike":
                (_, nnv) = sushi_rolls[int(i + 2)].values()
                dimsum += nnv[0]

        # Spares
        elif t == "spare":
            # Get next frame
            (_, nv) = sushi_rolls[int(i + 1)].values()
            dimsum += sum(v) + nv[0]

        # All the rest (regular or last)
        else:
            dimsum += sum(v)

    return dimsum
