from functionGenerator import *
from maintenance import *
from docx import *

import sys, getopt, random, math, datetime, time

def main(argv):
    exercises = []

    arguments = getParameters(argv)

    types ={'s': aufgabe_summe, \
        'p': aufgabe_produkt, \
        'c': aufgabe_chain,\
        'q':aufgabe_quotient
        }

    list_of_types = check_types(types, arguments[1])

    for choice in list_of_types:
        for i in range(arguments[0]):
            exerc = types[choice]()
            exercises.append(exerc)
            exerc =""    
    if arguments[2]:
         random.shuffle(exercises)        
    createFile(exercises,arguments[3],"Leiten Sie die folgenden Funktionen ab.")  

if __name__ == "__main__":
    main(sys.argv[1:])

