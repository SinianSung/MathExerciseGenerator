from rootGenerator import *
from maintenance import *

import sys, getopt, random, math, datetime, time


def main(argv):
    exercises = []

    arguments = getParameters(argv)

    types ={'s': square_free, \
        'e': simple_fraction, \
        'n': normal_fraction, \
        'h': hard_fraction
        }

    list_of_types = check_types(types, arguments[1])

    for choice in list_of_types:
        for i in range(arguments[0]):
            exerc = types[choice]()
            exercises.append(exerc)
            exerc =""    
    if arguments[2]:
         random.shuffle(exercises)        
    createFile( exercises,arguments[3]," Schreiben Sie die Wurzeln quadratfrei und die Nenner wurzelfrei!")  

if __name__ == "__main__":
    main(sys.argv[1:])

