#!/usr/bin/env python3
"""
Proyecto Polinomio de Taylor.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


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
    def poli(x):
        i=0
        global f
        while (i<n):
            if i!=0:
                dx = derivada(f)
                f = dx
                polinomio= polinomio + (dx(x0)*((x-x0)**i))/math.factorial(i)
            else: 
                polinomio= f(x0)
            i=i+1        
        return polinomio
    return poli


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    f = lambda x: math.cos(x)
    p = polinomio_taylor(f,0,3)
    print ("Valor Aproximado:", p(0.2))
