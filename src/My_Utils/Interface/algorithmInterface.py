import abc
import math
import random

class HeuristicAlgorithmInterface(metaclass=abc.ABCMeta):
    """
        Abstract class that represents the interface of the heuristic algorithm
        implementations. 
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'minimize') and 
                callable(subclass.load_data_source) or 
                NotImplemented)

    @abc.abstractmethod
    def minimize(self):
        """Start the heuristic algorithm process"""
        raise NotImplementedError
    
    def function(self, x: float, y: float) -> float:
        first_part = ((math.sin(x/180 - 4))/(((x*x)/100000) + 1))
        second_part = (x*x)/500000
        third_part = ((math.cos(y/100 - 1))/( ((y*y)/1000000) + 1))
        fourth_part = (y*y)/500000
        return first_part + second_part + third_part + fourth_part

    def generateRandomNumber(self, start, end) -> int:
        return random.randint(start, end) 