from random import choice


class RandomWalk:

    def __init__(self, points=5000):
        self.points = points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def walk(self):

        while len(self.x_values) < self.points:

            # X
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # Y
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position using last values stored into lists
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
