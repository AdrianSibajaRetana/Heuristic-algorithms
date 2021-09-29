from My_Utils.factory import HeuristicAlgorithmFactory
from My_Utils import constants
import sys

def executeAlgorithm(selected_option: int):
    factory = HeuristicAlgorithmFactory()
    AlgorithmSelected = factory.get_algorithm(selected_option)
    AlgorithmSelected.minimize()
    

def printOptions(dictionary: dict):    
    for key, value in dictionary.items():
        print(key, ': ', value)
    

def main():
    options = {
        constants.PARTICLE_SWARM: "Particle Swarm"
    }    
    is_looking_for_input = True    
    print("Select the algorithm you wish to use: ")
    while (is_looking_for_input):
        printOptions(options)        
        raw_user_input = input()
        try:
            numerical_user_input = int(raw_user_input)
        except:
            print("Input must be a number. Please try again.")
        else:
            if numerical_user_input in options:
                is_looking_for_input = False
                executeAlgorithm(numerical_user_input)
            else:
                print("Please enter a valid option.") 


if __name__ == "__main__":
    main()

    
