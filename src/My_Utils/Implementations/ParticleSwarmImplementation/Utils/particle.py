class Particle:
    current_solution = 0
    best_x = 0
    best_y = 0

    def __init__(self, x_position, y_position, velocity_x, velocity_y, current_solution):
        self.x = x_position
        self.y = y_position
        self.vx = velocity_x
        self.vy = velocity_y
        self.best_solution = current_solution

    def PrintParticle(self, particle_index):
        print(f"X{particle_index} = ({self.x: 3f}, {self.y: 3f}), f(x_{particle_index}) = {self.current_solution: 5f}")
