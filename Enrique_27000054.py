#!/usr/bin/env python3
"""
Proyecto Polinomio de Taylor.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""
from math import *



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

def factorial (k):
    if (k<=0):
        return 1
    else:
        return k*factorial(k-1)

def polinomio_taylor(f, x0, n):
    """
    Implementa y retorna el Polinomio de Taylor de grado n centrado en x0.

    Parámetros:
    f: función de variable real f(x).
    x0: punto centro del polinomio.
    n: grado del polinomio.
    """


    def segundo_polinomio(x):
        polinomio=0
        k=0
        global f
        while (k<n):
            if (k==0):
                polinomio=f(x0)
            else:
                derivacion= derivada(f)
                f=derivacion
                polinomio= polinomio + (derivacion(x0)*((x-x0)**k))/factorial(k)
            k=k+1
        return polinomio  

    return segundo_polinomio



if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    f = lambda x: sin(x);
    prueba = polinomio_taylor(f,0,8)
    print ("El valor real es: ", f(0.5))
    print ("El valor aproximado de taylor es: ", prueba(0.5))
    
