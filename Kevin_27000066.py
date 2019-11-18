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
    def polinomio(x):
        global f
        for c in range(n):
            if c != 0:
                sop = derivada(f)
                f = sop
                p += (sop(x0) * ((x - x0)**c)) / math.factorial(c)
            else:
                p = f(x0)
        return p            
    return polinomio

f = lambda x: math.sin(x)

if __name__ == '__main__':
    pr = polinomio_taylor(f,0,4)
    print("> Aproximación: ", pr(0.3))
    