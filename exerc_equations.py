
from docx import *
from equationGenerator import *
from maintenance import *
import sys, getopt, random, math, datetime, time



def main(argv):
    arguments = getParameters(argv)
    exercises = []

    types ={'b': exerciseLin, \
        'e': exerciseExp, \
        'l': exerciseLog, \
        't': exerciseTrig, \
        'q': exerciseQuad, \
        's': exerciseSystem, \
        'p': exercisePoly,  \
        'r': exerciseRation
        }

    list_of_types = check_types(types, arguments[1])

    for choice in list_of_types:
        for i in range(arguments[0]):
            exerc = types[choice]()
            exercises.append(exerc)
            exerc =""    
    if arguments[2]:
        random.shuffle(exercises)  

    createFile( exercises,arguments[3], 'Lösen Sie die Aufgaben')  

if __name__ == "__main__":
    main(sys.argv[1:])
