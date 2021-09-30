from My_Utils.Implementations.ParticleSwarmImplementation.Utils.constants import LOWER_BOUND, UPPER_BOUND
from ...Interface.algorithmInterface import HeuristicAlgorithmInterface
from My_Utils.Implementations.ParticleSwarmImplementation.Utils import constants
from My_Utils.Implementations.ParticleSwarmImplementation.Utils.particle import Particle


class ParticleSwarmAlgorithm(HeuristicAlgorithmInterface):
    # Internal variables for the particle swarm algorithm 
    particle_array = []
    """Array used for storing the particles"""
    stop_algorithm = False
    """Boolean used for the stop condition of the algorithm."""

    best_solution = float("inf")
    """Stores the best solution found by the particles."""
    best_x = 0
    """Stores the x coordinate of the best solution"""
    bext_y = 0
    """Stores the y coordinate of the best solution"""

    # Internal variables for the stopping condition of the algorithm.
    iterations_with_no_change = 0    
    lower_bound_best_answer = float("inf")
    upper_bound_best_answer = float("-inf")

    def __InitializeParticles(self):
        """
            Gives the initial values to the iteration's particles. 
        """
        for i in range(constants.PARTICLE_NUMBER):
            x = super().generateRandomNumber(constants.LOWER_BOUND, constants.UPPER_BOUND)
            y = super().generateRandomNumber(constants.LOWER_BOUND, constants.UPPER_BOUND)
            vx = super().generateRandomNumber(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
            vx = super().generateRandomNumber(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
            vy = super().generateRandomNumber(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
            p = Particle(x, y, vx, vy, self.best_solution)
            self.particle_array.append(p)
    
    def __AdjustVelocity(self, dimention: constants.Dimention, current_particle: Particle) -> float:
        v_i = 0
        r1 = super().generateRandomNumber(0,1)
        r2 = super().generateRandomNumber(0,1)
        p_i = 0
        x_i = 0
        g_i = 0
        if dimention == constants.Dimention.X_DIMENSION:
            v_i = current_particle.vx            
            p_i = current_particle.best_x
            x_i = current_particle.x
            g_i = self.best_x
        elif dimention == constants.Dimention.Y_DIMENSION:
            v_i = current_particle.vy          
            p_i = current_particle.best_y
            x_i = current_particle.y
            g_i = self.best_y
        new_velocity = constants.W*v_i + constants.C1*r1*(p_i - x_i) + constants.C2*r2*(g_i - x_i);
        return new_velocity

    def __AdjustParticleVelocity(self, current_particle: Particle):
        """
            Calls the helper methods to give the particle its new
            velocities for the next iteration.
        """
        current_particle.vx = self.__AdjustVelocity(constants.Dimention.X_DIMENSION, current_particle)
        current_particle.vy = self.__AdjustVelocity(constants.Dimention.Y_DIMENSION, current_particle)

    def __AdjustPosition(self, dimention: constants.Dimention, current_particle: Particle) -> float:
        x_i = 0
        v_i = 0
        new_position = 0

        if dimention == constants.Dimention.X_DIMENSION:        
            x_i = current_particle.x
            v_i = current_particle.vx     
        elif dimention == constants.Dimention.Y_DIMENSION:       
            x_i = current_particle.y
            v_i = current_particle.vy
        
        new_position = x_i + v_i

        if new_position < constants.LOWER_BOUND:        
            new_position = constants.UPPER_BOUND
        
        elif new_position > constants.UPPER_BOUND:        
            new_position = constants.LOWER_BOUND
        
        return new_position
        
    def __AdjustParticlePosition(self, current_particle: Particle):
        """
            Calls the helper methods to give the particle its new
            position for the next iteration. 
        """
        current_particle.x = self.__AdjustPosition(constants.Dimention.X_DIMENSION, current_particle)
        current_particle.y = self.__AdjustPosition(constants.Dimention.Y_DIMENSION, current_particle)

    def __PrintCurrentIteration(self, iteration_number: int):
        """
            Prints the information of the current iteration's particles.
        """
        print(f"Iteration {iteration_number}:\tG=({self.best_x: 5f}, {self.best_y: 5f}), f(G) = {self.best_solution: 7f}")
        particle_index = 1
        for particle in self.particle_array:
            particle.PrintParticle(particle_index)
            particle_index += 1
    
    def __EvaluateParticle(self, current_particle: Particle):
        """
            Grades the current particle according to the result given
            by a two variable mathematical function. 

            If the score graded is the best seen yet, the corresponding 
            values are overwritten.  
        """
        x = current_particle.x
        y = current_particle.y
        score = super().function(x, y)
        current_particle.current_solution = score
        if score < current_particle.best_solution:
            current_particle.best_solution = score
            current_particle.best_x = x
            current_particle.best_y = y
    
    def __EvaluateParticleSolution(self, current_particle: Particle):
        """
           Checks if the current particle's solution is better than the
           best solution found on the algorithm. 

           If this checks true, the new values are overwritten. 
        """
        score = current_particle.current_solution
        if score < self.best_solution:
            self.best_solution = score
            self.best_x = current_particle.x
            self.best_y = current_particle.y

    def __EvaluateStopingCondition(self):
        """
            Indicates that the algorithm should be stoped if the value
            has not changed significally in 50 iterations. 
        """
        limit = 0.001;
        if self.lower_bound_best_answer < self.best_solution and self.best_solution <= self.upper_bound_best_answer:
            self.iterations_with_no_change = self.iterations_with_no_change + 1
            if self.iterations_with_no_change == constants.MAX_ITERATIONS_WITHOUT_CHANGE:
                self.stop_algorithm = True        
        else:
            self.iterations_with_no_change = 0;
            self.lower_bound_best_answer = self.best_solution - limit
            self.upper_bound_best_answer = self.best_solution + limit

    def __PrintFinalIteration(self):
        """
            Prints the end results of the algorithm. 
        """
        print(f"Final iteration:\tG=({self.best_x: 5f}, {self.best_y: 5f}), f(G) = {self.best_solution: 7f}")

    def minimize(self):
        """
            Main loop of the particle swarm algorithm. 
        """
        self.__InitializeParticles()
        current_iteration = 1

        while(current_iteration <= constants.ITERATION_NUMBER and not self.stop_algorithm):

            for particle in self.particle_array:
                self.__EvaluateParticle(particle)
                self.__EvaluateParticleSolution(particle)
            
            self.__PrintCurrentIteration(current_iteration)

            for particle in self.particle_array:
                self.__AdjustParticleVelocity(particle)
                self.__AdjustParticlePosition(particle)
            
            self.__EvaluateStopingCondition()
            current_iteration += 1

        self.__PrintFinalIteration()
