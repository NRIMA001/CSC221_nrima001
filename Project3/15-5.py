from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

        """Refactoring"""
    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step


    def fill_walk(self):
        """Calculate all the points in the walk."""
    
        # Keep taking steps until the walk reaches the desired distance
        while len(self.x_values) < self.num_points:
        
            # Decide which direction to go and how far 
            x_step = self.get_step()
            y_step = self.get_step()
        
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
        
            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
        
            self.x_values.append(x)
            self.y_values.append(y)