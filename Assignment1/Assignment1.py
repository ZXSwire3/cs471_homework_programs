from typing_extensions import NamedTuple
import unittest


# Circle class used to represent a circle on a graph
class ctuple(NamedTuple):
    x: float
    y: float
    radius: float


def check_overlap(circle1, circle2):
    # Calculate the distance between the centers of the circles
    distance = ((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2) ** 0.5
    # Check if the distance is less than or equal to the sum of the radii
    return distance <= (circle1.radius + circle2.radius)


def dfs(circle, circles, visited):
    # Mark the current circle as visted
    visited.add(circle)
    # Explore the rest of the circles in the circle tuple
    for other_circle in circles:
        # Check if the other circle has not been visted but overlaps with the current circle
        if other_circle not in visited and check_overlap(circle, other_circle):
            # Recursively visit the other circle
            dfs(other_circle, circles, visited)


def check_cluster(circles):
    # If circles is empty, return false
    if not circles:
        return False
    # Initialize a set to keep track of visited circles
    visited = set()
    # Start DFS from first circle in tuple
    dfs(circles[0], circles, visited)
    # Check if all circles have been visited
    return len(visited) == len(circles)


class TestCluster(unittest.TestCase):
    def test_check_cluster(self):
        # Test case 1
        circle1 = ctuple(1, 3, 0.7)
        circle2 = ctuple(2, 3, 0.4)
        circle3 = ctuple(3, 3, 0.9)
        circles1 = (circle1, circle2, circle3)
        print(check_cluster(circles1))
        self.assertEqual(check_cluster(circles1), True)

        # Test case 2
        circle1 = ctuple(1.5, 1.5, 1.3)
        circle2 = ctuple(4, 4, 0.7)
        circles2 = (circle1, circle2)
        print(check_cluster(circles2))
        self.assertEqual(check_cluster(circles2), False)

        # Test case 3
        circle1 = ctuple(0.5, 0.5, 0.5)
        circle2 = ctuple(1.5, 1.5, 1.1)
        circle3 = ctuple(0.7, 0.7, 0.4)
        circle4 = ctuple(4, 4, 0.7)
        circles3 = (circle1, circle2, circle3, circle4)
        print(check_cluster(circles3))
        self.assertEqual(check_cluster(circles3), False)

        # Test case 4
        circle1 = ctuple(3, 6, 3)
        circle2 = ctuple(6.5, 3, 3)
        circle3 = ctuple(10, 6, 3)
        circle4 = ctuple(13.5, 3, 3)
        circle5 = ctuple(17, 6, 3)
        circles4 = (circle1, circle2, circle3, circle4, circle5)
        print(check_cluster(circles4))
        self.assertEqual(check_cluster(circles4), True)
