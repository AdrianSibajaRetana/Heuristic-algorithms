import abc

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