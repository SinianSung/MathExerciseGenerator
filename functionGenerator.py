from fractions import Fraction
from sympy import *
from sympy.solvers import solve

import math, random


def term_trig():
    trigfunktionen = ['sin(£)','cos(£)','sin(£)','cos(£)','tan(£)']

    return trigfunktionen[random.randint(0,2)]

def term_exp():
        r = random.random()
        if r<0.3:
                a = random.randint(2,5)
                return "{}**£".format(a)
        else:
                a=random.choice([-4,-3,-2,-1,1,2,3,4])
                return "exp({}*£)".format(a)

def term_log():
        r = random.random()
        if r<0.3:
                return "ln(£)"
        elif r < 0.7:
                return "log10(£)"
        else:
                b = random.randint(2,10)
                return "log(£,{})".format(b)

def term_root():
    n = random.choice([2,2,2,2,2,3])
    return "root(£,{})".format(n)

def term_potenz():
    a = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
    b = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
    c = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
    n = random.randint(0,3)
    m = random.randint(1,3)+n
    return "{}*£**{}+ {}*£**{}+{}".format(a,n,b,m,c)

def generateRandomFunction(loft):
        typus = random.choice(loft)
        if typus == 'pot':
                return term_potenz()
        elif typus == 'trig':
                return term_trig()
        elif typus =='log':
                return term_log()
        elif typus == 'exp':
                return term_exp()
        else:
                return term_root()
        

def aufgabe_summe():
    terma = term_potenz()
    termb = generateRandomFunction(['trig','pot','exp','root','log'])
    x = symbols('x')

    terma = terma.replace('£','x')
    termb = termb.replace('£','x')
    term = sympify(terma +'+'+ termb)
    fun = latex(simplify(term))
    deriv = latex(simplify(diff(term,x)))
    return (fun, deriv)   

def aufgabe_produkt():
        terma = generateRandomFunction(['trig','pot','root','pot'])
        termb = generateRandomFunction(['trig','pot','exp','root'])
        x = symbols('x')

        terma = terma.replace('£','x')
        termb = termb.replace('£','x')
        term = sympify('('+terma+ ')*(' +termb+')')
        terma_s = expand(sympify(terma))
        termb_s = expand(sympify(termb))
        fun = latex(simplify(term))
        deriv = latex(simplify(diff(term,x)))
        deriv_a = latex(expand(simplify(diff(terma_s,x))))
        deriv_b = latex(expand(simplify(diff(termb_s,x))))
        deriv_long ="\\left ("+deriv_a + "\\right ) \\cdot \\left ("+ latex(termb_s) +"\\right ) + \\left ("+latex(terma_s) + "\\right ) \\cdot \\left ("+ deriv_b +"\\right )"

        return (fun, deriv_long + " = "+ deriv)   

def aufgabe_quotient():
        terma = generateRandomFunction(['trig','pot','pot','exp'])
        termb = generateRandomFunction(['trig','pot','pot','pot'])
        x = symbols('x')

        terma_s = expand(sympify(terma.replace('£','x')))
        termb_s = expand(sympify(termb.replace('£','x')))
        termb_s_s =  sympify(termb.replace('£','x')+"**2")

        fun = "\\frac{"+latex(terma_s)+"}{"+ latex(termb_s)+'}'
        term = sympify("("+terma.replace('£','x')+") / ("+termb.replace('£','x')+")")
        deriv_a = latex(expand(simplify(diff(terma_s,x))))
        deriv_b = latex(expand(simplify(diff(termb_s,x))))
        deriv = latex(simplify(diff(term,x)))
        deriv_long ="\\frac{\\left ("+deriv_a + "\\right ) \\cdot \\left ("+ latex(termb_s) +"\\right ) - \\left ("+latex(terma_s) + "\\right ) \\cdot \\left ("+ deriv_b +"\\right ) }{("+ latex(termb_s)+ ")^2}"

        return (fun, deriv_long + " = " +deriv)       

def aufgabe_chain():
    x = symbols('x')
    outer = generateRandomFunction(['trig','exp','root'])
    inner = generateRandomFunction(['pot'])
    inner = inner.replace('£','x')
    outer = sympify(outer.replace('£',inner))
    fun = latex(simplify(outer))
    deriv = latex(simplify(diff(outer,x)))
    return (fun, deriv)