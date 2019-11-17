#!/usr/bin/env python3
"""
Proyecto Polinomio de Taylor.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math

def f(x):
    return math.sin(x)


def derivada(f, h = 0.01):
    """
    Retorna la función derivada de f dado un h.

    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _


def polinomio_taylor(f, x0, n):
    """
    Implementa y retorna el Polinomio de Taylor de grado n centrado en x0.

    Parámetros:
    f: función de variable real f(x).
    x0: punto centro del polinomio.
    n: grado del polinomio.
    """
    x=0.30
    i=0
    result=0
    while(i<n):
        if (i==0):
            result=f(x0)
            ff=derivada(f)   
        elif(i==1):
            result=result+ff(x0)*(x-x0)**i
            ff=derivada(ff)
        else:
            result=result+ff(x0)*(x-x0)**i/math.factorial(i)
            ff=derivada(ff)
        i=i+1
        if(i==n):
            result=result+ff(x0)*(x-x0)**i/math.factorial(i)

    polinomio=result

    return polinomio


if __name__ == '__main__':
    
    print ("el Aproximado es:"+" "+str(polinomio_taylor(f,0,4)))