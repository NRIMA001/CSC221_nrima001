from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far.
            x_step = get_step()
            y_step = get_step()

            # Reject moves that go nowhere
            if x_step != 0 or y_step != 0:

                # Calculate next x and y
                next_x = self.x_values[-1] + x_step
                next_y = self.y_values[-1] + y_step

                self.x_values.append(next_x)
                self.y_values.append(next_y)

"""Modified Random Walks. """
def get_step():
    direction = choice([1, -1])
    distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

    return direction * distance