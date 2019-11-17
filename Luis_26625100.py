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

    def factorial(n):
        if n < 2:
            return 1
        else:
            return n * factorial(n-1)


    def polynomial(x):
        function = f(x0)
        derv = f
        i = 1

        while i <= n:
            derv = derivada(derv)
            function = function + (derv(x0) * (((x - x0)**i) / factorial(i)))
            i += 1

        return function

    return polynomial


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    f = lambda x: math.sin(x)
    x = 0.3
    print("El valor aproximado es de:", polinomio_taylor(f, 0, 4)(x))
