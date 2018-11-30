from fractions import Fraction
import math
import random
from sympy import *
from sympy.solvers import solve


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

def getNumber(max):
    a=int(random.randrange(1,max))
    if random.randrange(2) ==0:
        return -a
    else:
        return a

def formula(num):
    if num==1:
        return ""
    else:
        return str(num)


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

def ausklammernLeft(a,b,A,B):
    """"
    generates a term for factoring out
    aBx^A+1 + a b x^A 
    """
    
    return formula(a*b) +" x^"+formula(A+1)+" + " + formula(a*B) +" x^"+formula(A)


def ausklammernRight(a,b,A,B):
    """
    generates a term for factoring out
    ax^A (Bx+b) 
    """

    return formula(a) +" x^"+formula(A)+" \\cdot\\left (" + formula(B) +" x +"+str(b) + "\\right)"

def summe(a,b,A,B):
    """
        ABx^2 + (Aa+Bb)x+ab
    """
    return formula(A*B)+" x^2 +"+ str(A*a+B*b) + " x + " + str(a*b)

def produkt(a,b,A,B):
    """

    """
    return "\\left(" + formula(A) +" x +" +str(a) + "\\right)  \\left( "+ formula(B)+"x + " + str(b) + "\\right)"

def binom_sum(a,A):
    """

    """
    return latexFraction(A*A) + "x^2 +" + latexFraction(2*a*A) + "x + " + latexFraction(a*a)

def binom_sum_3(a,A):
    """

    """
    return latexFraction(A*A) + "x^2 "  "- " + latexFraction(a*a)

def binom_prod(a,A):
    """

    """
    return  "\\left(" + latexFraction(A) + "x +" + latexFraction(a) + "\\right) ^2 "

def binom_prod_3(a,A):
    """

    """
    return  "\\left(" + latexFraction(A) + "x +" + latexFraction(a) + "\\right) \\left(" + latexFraction(A) + "x -" + latexFraction(a) + "\\right) "

def factor_out():
    a = getNumber(10)
    b = getNumber(20)
    A = getNumber(4)
    B = getNumber(4)

    leftside = ausklammernLeft(a,b,A,B)
    rightside =ausklammernRight(a,b,A,B)

    return (leftside, rightside)

def mult():
    a = getNumber(10)
    b = getNumber(20)
    A = getNumber(4)
    B = getNumber(4)

    rightside = ausklammernLeft(a,b,A,B)
    leftside =ausklammernRight(a,b,A,B)

    return (leftside, rightside)

def prod_mult():
    """
    produkt in summe ausmultiplizieren
    """
    a = getNumber(10)
    b = getNumber(10)
    A = getNumber(4)
    B = getNumber(4)

    summ = summe(a,b,A,B)
    prod =produkt(a,b,A,B)

    return (summ, prod)

def sum_to_factor():
    """
    Version _ Summe in Faktoren zerlegen
    """
    a = getNumber(10)
    b = getNumber(10)
    A = getNumber(4)
    B = getNumber(4)

    summ = summe(a,b,A,B).replace("+-", "-")
    prod =produkt(a,b,A,B).replace("+-", "-")

    return (prod, summ)

def binom_to_factor():
    """
    binom in faktoren zerlegen
    """

    a = getNumber(12)
    A = getNumber(6)


    summ = binom_sum(a,A)
    prod = binom_prod(a,A)

    return (summ, prod)

def binom_mult():
    """
    binom ausmultiplizieren
    """
    a = getNumber(12)
    A = getNumber(5)


    summ = binom_sum(a,A).replace("+-","-")
    prod = binom_prod(a,A).replace("+-","-")
    prod = prod.replace("(1x", "(x")
    return (prod, summ)


def binom_mult_3():
    """
    binom ausmultiplizieren
    """
    a = getNumber(12)
    A = getNumber(5)


    summ = binom_sum_3(a,A).replace("+-","-")
    prod = binom_prod_3(a,A).replace("--","+")
    prod = prod.replace("(1x", "(x")
    prod = prod.replace("+-", "-")
    return (prod, summ)

def binom_mult_s():
    """
    binom ausmultiplizieren
    """

    a = getNumber(12)
    A = 1


    summ = binom_sum(a,A).replace("+-", "-")
    prod = binom_prod(a,A).replace("+-", "-")
    prod = prod.replace("(1x", "(x")

    return (prod, summ)


def termprodukt():
    a = random.randrange(10)
    b = random.randrange(10)

    exprA = sympify("x+"+a)
    exprB = sympify("x+"+b)

    summ = latex(simplify(expand(exprA*exprB)))
    prod = latex(simplify(exprA*exprB))
    return (summ, prod)

def trinom_s(level = 0):
    if level ==0:
        a = random.randrange(1,10)
        b = random.randrange(1,10)
    else:
        a = random.randrange(100)
        b = random.randrange(100)

    exprA = sympify("x+"+str(a))

    summ = latex(simplify(expand(exprA*exprA)))
    prod = latex(simplify(exprA*exprA))
    return (summ, prod)

def trinom(level = 0):
    if level ==0:
        a = getNumber(12)
        b = getNumber(12)
    else:
        a = random.randrange(100)
        b = random.randrange(100)

    exprA = sympify("x+"+ str(a))
    exprB = sympify("x+" + str(b))

    summ = latex(simplify(expand(exprA*exprB)))
    prod = latex(simplify(exprA*exprB))
    return (summ, prod)