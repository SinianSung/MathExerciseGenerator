from fractions import Fraction
from sympy import *
from sympy.solvers import solve

import math, random


def generateFraction(a=10,b=10):
    num= random.randrange(1,a)
    if random.randrange(2) ==0:
        num =  -num
    denom = random.randrange(1,b)
    return Fraction(num, denom)

def latexFraction(A, pi=False):
    if A.numerator ==0:
        return "0"
    elif A.denominator ==1:
        return str(A.numerator)
    else:
        if pi:
            return "\\frac\x7b "+ str(A.numerator) +"\pi\x7d\x7b"+ str(A.denominator)+"\x7d"
        else:
            return "\\frac\x7b"+ str(A.numerator) +"\x7d\x7b"+ str(A.denominator)+"\x7d"


def simple_fraction():
    """
        a*sqrt(b*c*x^n)

    """
    a = random.choice([1,2,3,4,5,6,7,8,9])
    b = random.choice([2,3,5,6,11])
    c = random.choice([2,3,5,6,7,10])

    gcd = math.gcd(a,b*c)

    term_latex = "\\frac{{ {} }}{{ {} \\sqrt{{ {} }}  }}".format(a,b,c)
    if a//gcd == 1:
        term_s = "\\frac{{ \\sqrt{{ {} }}  }}{{ {}  }}".format(c,b*c//gcd)
    else:
        term_s = "\\frac{{ {} \\sqrt{{ {} }}  }}{{ {}  }}".format(a//gcd,c,b*c//gcd)

    return (term_latex, term_s)   
    
def normal_fraction():
    """
        a*sqrt(b*c*x^n)

    """
    a = random.choice([1,2,3,4,5,6,7,8,9])
    c = random.choice([2,3,5,6,7,10])
    b = c+random.choice([1,2,3,5,6,7])
    is_plus = random.choice([True, False])

    gcd = math.gcd(a,b-c)

    if is_plus:
        sign='+'
        revsign='-'
    else:
        sign='-'
        revsign='+'
    
    term_latex = "\\frac{{ {} }}{{ \\sqrt{{ {} }} {} \\sqrt{{ {} }}  }}".format(a,b,sign, c)
    if a//gcd == 1:
        if (b-c)//gcd ==1:
            term_s = " \\sqrt{{ {} }}  {} \\sqrt{{ {} }} ".format(b,revsign,c)
        else:
            term_s = "\\frac{{ \\sqrt{{ {} }}  {} \\sqrt{{ {} }} }}{{ {}  }}".format(b,revsign,c, (b-c)//gcd)
    else:
        if (b-c)//gcd ==1:
            term_s = "{} (\\sqrt{{ {} }} {} \\sqrt{{ {} }} ) ".format(a//gcd,b,revsign,c)
        else:
            term_s = "\\frac{{ {} (\\sqrt{{ {} }} {} \\sqrt{{ {} }} ) }}{{ {}  }}".format(a//gcd,b,revsign,c,(b-c)//gcd)

    return (term_latex, term_s)   


def square_free():
    """
        a*sqrt(b*c*x^n)

    """
    symb =random.choice(['a','b','c','x','y','p'])
    a = random.choice([2,3,4,5,6,7,8,9])
    b = random.choice([2,3,5,6,11])
    c = random.choice([2,3,4,5,6,8,9,10])
    n = random.choice([1,2,3,4,5,6])
    if n==1:
        term_latex ="{}\\sqrt{{ {} x }}".format(a,b*c*c)
        term_s ="{} \\sqrt{{ {} x }}".format(a*c,b)
    elif n%2==0:
        term_latex ="{}\\sqrt{{ {} x^{} }}".format(a,b*c*c,n)
        if n==2:
            term_s ="{} x \\sqrt{{ {}  }}".format(a*c,b)
        else:
            term_s ="{}  x^{} \\sqrt{{ {}  }}".format(a*c,n//2,b)
    else:
        term_latex ="{}\\sqrt{{ {} x^{} }}".format(a,b*c*c,n)
        if n==3:
            term_s ="{} x \\sqrt{{ {} x }}".format(a*c,b)
        else:
            term_s ="{} x^{} \\sqrt{{ {} x }}".format(a*c,(n-1)//2,b)

    term_s = term_s.replace('x',symb)
    term_latex = term_latex.replace('x',symb)     

    return (term_latex, term_s)

def hard_fraction():
    a = random.choice([2,3,5,6,7,8,10,11,12])
    b = a+random.choice([1,2,3,4,5])
    c = random.choice([2,3,4,5,6,8,9,10])
    d = c+random.choice([1,2,3,5])


    if random.choice([0,1])==0:
        zaehler = "sqrt({}) + sqrt({})".format(b,a)
        zaehler_latex = "\\sqrt{{ {} }} + \\sqrt{{ {} }}".format(b,a)
    else:
        zaehler = "sqrt({}) - sqrt({})".format(b,a)
        zaehler_latex = "\\sqrt{{ {} }} - \\sqrt{{ {} }}".format(b,a)

    if random.choice([0,1])==0:  
        nenner = "sqrt({}) + sqrt({})".format(d,c)
        nenner_latex = "\\sqrt{{ {} }} + \\sqrt{{ {} }}".format(d,c)
        faktor = "sqrt({}) - sqrt({})".format(d,c)       
    else:
        nenner = "sqrt({}) - sqrt({})".format(d,c)
        nenner_latex = "\\sqrt{{ {} }} - \\sqrt{{ {} }}".format(d,c)
        faktor = "sqrt({}) + sqrt({})".format(d,c)       

    zaehler_s = sympify(zaehler)
    nenner_s = sympify(nenner)
    faktor_s = sympify(faktor)
    term_latex = "\\frac{ "+zaehler_latex+"}{"+nenner_latex+"}"

    numerical_value = N(zaehler_s/nenner_s,3)

    if d-c ==1:
        term_s = latex(expand(zaehler_s*faktor_s))
    else:
        term_s = "\\frac{{ "+latex((zaehler_s*faktor_s))+"}}{{"+str(d-c)+"}}"

    return (term_latex, term_s)
