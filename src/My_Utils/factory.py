from My_Utils.Implementations.particleSwarm import ParticleSwarmAlgorithm
from My_Utils import constants

class HeuristicAlgorithmFactory:
    def get_algorithm(self, algorithm_selected: int):
        if algorithm_selected == constants.PARTICLE_SWARM:
            return ParticleSwarmAlgorithm()
        else:
            raise ValueError(format)