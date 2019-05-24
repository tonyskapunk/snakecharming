# -*- coding: utf-8 -*-

import pytest
from bowling import score

# On the left most side is the expected total... Then, there are ten pairs (possibly
# groups) of numbers. These
# numbers represent how many pins were knocked down during each roll.
TESTS = [
    # # All numbers
     (61, [['4', '3'], ['2', '1'], ['2', '3'], ['7', '1'], ['3', '6'], ['2', '2'], ['8',
'1'], ['6', '3'], ['2', '3'], ['1', '1']]),
    # # dashes
     (40, [['4', '3'], ['-', '1'], ['2', '-'], ['7', '1'], ['-', '6'], ['2', '-'], ['8',
'-'], ['6', '-'], ['-', '-'], ['-', '-']]),
    # # Spares
     (69, [['4', '3'], ['9', '/'], ['2', '-'], ['7', '/'], ['-', '6'], ['2', '/'], ['8',
'-'], ['6', '-'], ['-', '-'], ['-', '-']]),
    # # Strikes
     (87, [['X', '-'], ['2', '6'], ['X', '-'], ['7', '2'], ['X', '-'], ['-', '3'], ['X',
'-'], ['-', '-'], ['3', '2'], ['1', '1']]),
    # # Spares followed by Strikes
     (112, [['4', '3'], ['2', '6'], ['6', '/'], ['X', '-'], ['3', '3'], ['7', '/'], ['2',
'1'], ['7', '/'], ['X', '-'], ['3', '2']]),
    # # Strikes followed by Spares
     (118, [['4', '3'], ['2', '6'], ['X', '-'], ['3', '/'], ['3', '3'], ['X', '-'], ['2',
'/'], ['7', '/'], ['3', '6'], ['3', '2']]),
    # # Strikes followed by Strikes
     (135, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2',
'1'], ['7', '2'], ['2', '3'], ['3', '2']]),
    # # Spares in last set
    (146, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2',
'1'], ['7', '2'], ['2', '3'], ['3', '/', '6']]),
    # # Strikes in last set
    (149, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2',
'1'], ['7', '2'], ['2', '3'], ['X', '7', '2']]),
    # # Strikes and Spares in last set
     (150, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2',
'1'], ['7', '2'], ['2', '3'], ['X', '7', '/']]),
    # # All Strikes
     (300, [['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X',
'-'], ['X', '-'], ['X', '-'], ['X', 'X', 'X']])
        ]

# Evaluates the code. Probably best if this is not modified
@pytest.mark.parametrize("expected,rolls", TESTS)
def test_scores(expected, rolls):
    assert score(rolls) == expected

pytest.main()

