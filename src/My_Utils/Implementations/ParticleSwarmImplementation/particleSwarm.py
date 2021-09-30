from My_Utils.Implementations.ParticleSwarmImplementation.Utils.constants import LOWER_BOUND, UPPER_BOUND
from ...Interface.algorithmInterface import HeuristicAlgorithmInterface
from My_Utils.Implementations.ParticleSwarmImplementation.Utils import constants
from My_Utils.Implementations.ParticleSwarmImplementation.Utils.particle import Particle


class ParticleSwarmAlgorithm(HeuristicAlgorithmInterface):
    particle_array = []
    stop_algorithm = False
    best_solution = float("inf")
    best_x = 0
    bext_y = 0

    def InitializeParticles(self):
        for i in range(constants.PARTICLE_NUMBER):
            x = super().generateRandomNumber(constants.LOWER_BOUND, constants.UPPER_BOUND)
            y = super().generateRandomNumber(constants.LOWER_BOUND, constants.UPPER_BOUND)
            vx = super().generateRandomNumber(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
            vx = super().generateRandomNumber(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
            vy = super().generateRandomNumber(constants.MIN_VELOCITY, constants.MAX_VELOCITY)
            p = Particle(x, y, vx, vy, self.best_solution)
            self.particle_array.append(p)
    
    def AdjustParticleVelocity(self, current_particle: Particle):
        pass

    def AdjustParticlePosition(self, current_particle: Particle):
        pass

    def PrintCurrentParticleGeneration(self, iteration_number: int):

        print(f"Iteration = {iteration_number}:\tG=({self.best_x: 5f}, {self.best_y: 5f}), f(G) = {self.best_solution: 7f}")
        particle_index = 1
        for particle in self.particle_array:
            particle.PrintParticle(particle_index)
            particle_index = particle_index + 1
    
    def EvaluateParticle(self, current_particle: Particle):
        x = current_particle.x
        y = current_particle.y
        score = super().function(x, y)
        current_particle.current_solution = score
        if score < current_particle.best_solution:
            current_particle.best_solution = score
            current_particle.best_x = x
            current_particle.best_y = y
    
    def EvaluateParticleSolution(self, current_particle: Particle):
        score = current_particle.current_solution
        if score < self.best_solution:
            self.best_solution = score
            self.best_x = current_particle.x
            self.best_y = current_particle.y



    def minimize(self):
        self.InitializeParticles()
        current_iteration = 1
        while(current_iteration <= constants.ITERATION_NUMBER and not self.stop_algorithm):

            for particle in self.particle_array:
                self.EvaluateParticle(particle)
                self.EvaluateParticleSolution(particle)
            
            self.PrintCurrentParticleGeneration(current_iteration)

            for particle in self.particle_array:
                self.AdjustParticleVelocity(particle)
                self.AdjustParticlePosition(particle)




        

