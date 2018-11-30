from fractions import Fraction
import math
import random

def generateFraction(a=10,b=10):
    num= random.randrange(1,a)
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

def linEquation(A,B,C,D):
    """
    generates linear equation A*x + B = C*x + D
    """
    eq =""
    eq = latexFraction(A) +"\cdot x +" + latexFraction(B) + " = " + latexFraction(C) + "\cdot x + " + latexFraction(D)
    return eq

def linSolution(A,B,C,D):
    """
    generates Solution for lineare equation  A*x + B = C*x + D
    x = (D-B)/(A-C)
    """
    if C-A ==0:
        sol =("keine Lösung","keine Lösung")
    else:
        sol = "x = " + latexFraction((D-B)/(A-C))+" \\approx " +str(round(float((D-B)/(A-C)),4))
    return sol

def rationalEquation(param):
    """

    """
    if param[0] == 0:
        part1 = "\\frac{"+str(param[1])
    else:
        part1 = "\\frac{"+ str(param[0])+"\cdot x+ "+str(param[1])

    if param[5] == 0:
        part2 = "+"+str(param[5])
    else:
        part2 = ""
    
    eq = part1+"}{"+str(param[2]) +"\cdot x +"+str(param[3])+ "} = " \
        + "\\frac{"+ str(param[4])+"\cdot x"+part2 +"}{"+str(param[6]) +"\cdot x +"+str(param[7])+"}"
    return eq

def rationalSolution(param):
    A = Fraction(param[0]*param[6]-param[2]*param[4],1)
    B = Fraction(param[1]*param[6]+param[7]*param[0]-param[2]*param[5]-param[3]*param[4],1)
    C = Fraction(param[1]*param[7]-param[3]*param[5],1)
    return quadSolution(A, B, C, 0, 0)

def systemEquation(A,B,D,E,x,y):
    """
    generates an system of 2 equations
    aX+bY=c
    dX+eY=f
    """
    C = A*x+B*y
    F = D*x+E*y
    eq =  latexFraction(A) +" \cdot x  + "+latexFraction(B)+"\cdot y = "+ latexFraction(C) \
        + "; " + latexFraction(D) + " \cdot x + " +latexFraction(E) \
        + " \cdot y =" + latexFraction(F) 
    return eq

def systemSolution(A,B,D,E,x,y):
    """
    generates the Solution of Ax+By=C. Dx+Ey=F
    """
    sol = "x = " + latexFraction(x) + " ,  y = " + latexFraction(y)+" \\approx " \
    " " + str(round(float(x),4)) + " ,  y = " + str(round(float(y),4))
    return sol

def logEquation(b,n,A,B):
    """
    Generates Equations for log with
    b,n natural numbers, A,B Fractions
    """
    eq = "\log_\x7b"+str(b)+"\x7d \x7b (" \
        + latexFraction(A)+"\cdot x +" \
        + latexFraction(B)+")\x7d = "+str(n)
    return eq

def logSolution(b,n,A,B):
    """
    Generates Solutions for log_b(A*x+B)=n with
    b,n natural numbers, A,B Fractions
    result tupel: (String, float)
    """
    numerical_value = "x = {}".format(round(float((b**n-B)/A),4))
    sol = "x = {}".format(latexFraction((b**n-B)/A))+" \\approx "+ numerical_value 
    return sol

def expEquation(a,b,n,A,B):
    """
    generates Equation of the form a*A^x = b*B^(x+n)
    a,b,A,B Fractions, n natural Number
    """
    eq =  latexFraction(a)+"\\cdot\\left (" \
    + latexFraction(A)+"\\right )^x=" \
    + latexFraction(b)+"\cdot\\left (" \
    + latexFraction(B)+"\\right )^\x7bx+"+str(n) +"\x7d"
    return eq

def expSolution(a,b,n,A,B):
    """
    generates Solutions for a*A^x = b*B^(x+n)
    a,b,A,B Fractions, n natural Number
    """
    if a ==0:
        numeric_value = "keine Lösung"
        sol = (numeric_value, numeric_value)
    else:
        numerical_value = "x = {}".format(round( math.log(A/B,b/a*B**n),4))
        sol = "x = \log_\x7b"+latexFraction(A/B)+"\x7d("+latexFraction(b/a*B**n)+")"+" \\approx "+ numerical_value
    return sol

def trigEquation(A,B,v,fun="sin"):
    v=0
    if fun == "sin":
        eq = "\sin \\left ("+latexFraction(A)+" \cdot x + "+latexFraction(B) +" \\right ) ="+ str(v)
    elif fun == "cos":
        eq = "\cos \\left ("+latexFraction(A)+" \cdot x + "+latexFraction(B) +" \\right ) ="+ str(v)
    elif fun == "tan":
        eq = "\tan \\left ("+latexFraction(A)+" \cdot x + "+latexFraction(B) +" \\right ) ="+ str(v)
    else:
        eq = ""
    return eq

def trigSolution(A,B,v,fun="sin"):
    if fun == "sin":
        if v ==0:
            sol = "x = {}".format(round(float(-B/A),4))
            sol_string ="x = "+ latexFraction(-B/A, True) + " +"+latexFraction(1/A, True)+"\cdot k"
        else:
            sol = "x = {}".format(round(float(-B/A),4))
            sol_string ="x = "+ latexFraction(-B/A, True) + " +"+latexFraction(1/A, True)+"\cdot k"
    elif fun == "cos":
        if v ==0 :
            sol = "x = {}".format(round(float(math.pi/(2*A)-B/A),4))
            sol_string = "x = "+latexFraction(1/(2*A),True)+" +"+latexFraction(-B/A) + " + "+latexFraction(1/A, True)+" \cdot k"
        else:
            sol = "x = {}".format(round(float(math.pi/(2*A)-B/A),4))
            sol_string = "x = "+latexFraction(1/(2*A),True)+" +"+latexFraction(-B/A) + " + "+latexFraction(1/A, True)+" \cdot k"           
    else:
        pass

    numerical_value = "x = {}".format(round(float(-B/A),4))
    return sol_string+" \\approx "+ numerical_value

def quadEquation(A,B,C,D,E):
    """

    """
    eq = latexFraction(A) + "\cdot x^2 + " + latexFraction(B) \
    + "\cdot x + " + latexFraction(C) + " = "+ latexFraction(E) +"\cdot x + "+latexFraction(D)
    return eq

def quadSolution(A,B,C,D,E):
    diskr = (B-E)*(B-E) -4*A*(C-D)
    if A == 0:
        sol = "x = " + latexFraction((B-E)/(C-D))
        numerical_value = "x = {}".format(round((B-E)/(C-D)))
        return (sol,numerical_value)
    if diskr/(4*A) >0:
        sol = "x = "+latexFraction(-(B-E)/(2*A)) + "\pm \sqrt {"+ latexFraction(diskr/(4*A)) + "}"
        #numerical_value = 0
        numerical_value = "x_1 = {}, x_2 = {}".format(round(-(B-E)/(2*A) + math.sqrt(diskr/(4*A)),4),round(-(B-E)/(2*A) - math.sqrt(diskr/(4*A)),4))
    elif diskr ==0:
        sol = latexFraction(-(B-E)/(2*A))
        numerical_value = float(-(B-E)/(2*A))
    else:
        sol ="keine Lösung, D = " + latexFraction(diskr/(4*A))
        numerical_value = "keine Lösung"

    return sol+" \\approx "+ numerical_value

def polyEquation(a,B,n):
    """
    generates an equation that can be factorised
    a*(x-b)(x-n)*x =x^grad + =0
    """
    a_3 = a
    a_2 =  (a*B+a*n)
    a_1 = a*B*n
    equ = str(a_3) + " \cdot x^3" + " -" + latexFraction(a_2) + "\cdot x^2 +" \
        + latexFraction(a_1) + "\cdot x = 0"
    return equ

def polySolution(a,B,n):
    numeric_value = "x_1 = "+ str(round(float(B),4)) + ", x_2 = "+ str(n) + ", x_3 = 0"
    sol = "x_1 = "+ latexFraction(B) + ", x_2 = "+ str(n)+ ", x_3 = 0"
    return sol+" \\approx "+ numeric_value
    
def exercisePoly():
    a = random.randrange(1,5)
    B = generateFraction(10,10)
    n = random.randrange(1,5)
    equ = polyEquation(a,B,n)
    sol = polySolution(a,B,n)
    return (equ, sol)

def exerciseQuad():
    A = generateFraction(10,5)
    B = generateFraction(10,5)
    C = generateFraction(10,5)
    D = generateFraction(10,2)
    E = generateFraction(5,5)
    equ = quadEquation(A,B,C,D,E)
    sol = quadSolution(A,B,C,D,E)
    return (equ, sol)

def exerciseSystem():
    A = generateFraction(10,10)
    B = generateFraction(10,10)
    D = generateFraction(10,10)
    E = generateFraction(10,10)
    x = generateFraction(10,5)
    y = generateFraction(10,5)
    equ = systemEquation(A,B,D,E,x,y)
    sol = systemSolution(A,B,D,E,x,y)
    return (equ, sol)

def exerciseTrig():
    A = generateFraction()
    B = generateFraction()
    v=random.choice([0,Fraction(1,2)])
    trig = random.choice(['sin', 'cos'])
    equ = trigEquation(A,B,v,trig)
    sol = trigSolution(A,B,v,trig)
    return (equ, sol)

def exerciseExp():
    A = generateFraction(10,10)
    B = generateFraction(10,10)
    b = generateFraction(10,10)
    a = generateFraction(10,10)
    n = random.randrange(2,5)
    equ = expEquation(a,b,n,A,B)
    sol = expSolution(a,b,n,A,B)
    return (equ, sol)

def exerciseLog():
    A = generateFraction()
    B = generateFraction()
    b = random.randrange(2,5)
    n = random.randrange(2,5)
    equ = logEquation(b,n,A,B)
    sol = logSolution(b,n,A,B)
    return (equ, sol)

def exerciseLin():
    A = generateFraction()
    B = generateFraction()
    C = generateFraction()
    D = generateFraction()
    equ = linEquation(A,B,C,D)
    sol = linSolution(A,B,C,D)
    return (equ, sol)

def exerciseRation():
    a = random.randrange(0,5)
    b = random.randrange(1,8)
    c = random.randrange(1,3)
    d = random.randrange(1,5)
    e = random.randrange(1,5)
    f = random.randrange(0,5)
    g = random.randrange(1,2)
    h = random.randrange(1,5)
    param = [a,b,c,d,e,f,g,h]
    equ = rationalEquation(param)
    sol = rationalSolution(param)
    return (equ, sol)
