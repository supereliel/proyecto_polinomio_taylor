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
        j         = 0
        resultado = 0
        f_actual  = None
        while(j < n):
            if(j == 0):
                resultado += f(x0)
                f_actual   = f
            else:
                dj         = derivada(f_actual)
                f_actual   = dj
                resultado += ( (dj(x0) * math.pow((x-x0), j)) / math.factorial(j) )
            j += 1
        return resultado
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    f1 = lambda x: math.sin(x)
    #f1 = lambda x: 1/(1+x)
    pt = polinomio_taylor(f1, 0, 4)
    print("VALOR APROXIMADO UTILIZANDO POLINOMIO DE TAYLOR: ", pt(0.5))