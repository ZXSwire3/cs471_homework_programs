from typing_extensions import NamedTuple
from sympy import *
from IPython.display import display, Math
import random
import unittest


# Point class used to represent a point on a graph
class Point(NamedTuple):
    x: float
    y: float


# Define 'x' as a symbol for use in mathematical calculations
x = symbols('x')


def hill_climbing(function, state_space, step_size, start_point, max_sideways_moves=100):
    print("\tStart point:", start_point)

    # Create current at start_point and calculate y-value
    current_point = Point(start_point, function.subs(x, start_point))

    # Intialize step counter
    step_counter = 0
    # Initialize sideways moves counter
    sideways_moves = 0

    # Start Hill Climb Loop
    while True:
        # Intialize neighboring points
        previous_point = Point(current_point.x - step_size, function.subs(x, current_point.x - step_size))
        next_point = Point(current_point.x + step_size, function.subs(x, current_point.x + step_size))
        # Intialize array that holds the next and previous neighbors
        neighbors = [previous_point, next_point]

        move_made = False
        # Check neighbor's y-value
        for neighbor in neighbors:
            # Check if neighbor is within the state space
            if state_space[0] <= neighbor.x <= state_space[1]:
                # Check if neighbor's y-value is greater than the current point
                if neighbor.y > current_point.y:
                    # Set current point to the neighboring point
                    current_point = neighbor
                    move_made = True
                    # Reset sideways moves to 0
                    sideways_moves = 0
                    # Exit neighbor loop
                    break
                # Check if neighbor's y-value is the same as the current point
                elif neighbor.y == current_point.y:
                    # Check if the number of sideways moves is less than the maximum
                    if sideways_moves < max_sideways_moves:
                        # Increment sideways moves
                        sideways_moves += 1
                        # Set current point to the neighboring point
                        current_point = neighbor
                        move_made = True

                    # Exit neighbor loop
                    break

        # If move was made, increment step_counter
        if move_made:
            step_counter += 1
        # If no move was made, exit the loop
        else:
            break

    print("\tSteps taken:", step_counter)

    # Round the results to a reasonable precision
    current_point = Point(round(current_point.x, 10), round(current_point.y, 10))

    return current_point.x, current_point.y


class TestHillClimbing(unittest.TestCase):
    def test_hill_climbing(self):
        # Test case 1
        function = 2 - x ** 2
        state_space = [-5, 5]
        step_size = 0.5
        start_point = state_space[0]
        print(hill_climbing(function, state_space, step_size, start_point))
        self.assertEqual(hill_climbing(function, state_space, step_size, start_point), (0, 2))
    # Initialize variables for hill_climbing function
    function = 2-x**2
    state_space = [-5,5]
    step_size = 0.5
    start_point = state_space[0]

    # Print function using latex
    display(Math(f' f(x) = {latex(function)}'))

    # Run hill climbing algorithm
    results = hill_climbing(function, state_space, step_size, start_point)

    # Print results
    print("\nLocal Max:")
    display(Math(f' f({latex(results[0])}) = {latex(results[1])}'))