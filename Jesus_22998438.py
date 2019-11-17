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
        acum = 0
        Df = f
        for i in range(n+1):
            acum += ((Df(x0))/(math.factorial(i)))*((x-x0)**(i))
            Df = derivada(Df)
        return acum
    
    return polinomio


if __name__ == '__main__':
    er = lambda a,b: math.fabs((a-b)/a)

    g = lambda x: math.log(x)    

    t = polinomio_taylor(g,1,4)

    val = 1.2

    print('Valor real:',g(val))
    print('Valor aproximado:',t(val))
    print('Error relativo:',er(t(val),g(val)))
