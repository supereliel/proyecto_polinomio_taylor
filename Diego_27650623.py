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
        p=f(x0) 
        for i in range(n):  
            if(i==0):
                derivada_a = derivada(f)
                p = p + (derivada_a(x0) * (x-x0))
            else:
                derivada_a = derivada(derivada_a)
                p = p + ((derivada_a(x0) * (x-x0)**(i+1)) / math.factorial(i))
        return p         
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor. Probado con el ejemplo dado en la clase
    f = lambda x: math.sin(x)
    x0=0
    n = 4    
    p = polinomio_taylor(f,x0,n)
    x=0.3
    print ("\n"+"POLINOMIO DE TAYLOR:")
    print(" -Valor aproximado:",p(x))
    print(" -Valor real:", f(x))
    print(" -Error relativo", f(x)-p(x))
    pass