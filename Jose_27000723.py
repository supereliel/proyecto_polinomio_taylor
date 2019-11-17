#!/usr/bin/env python3
# coding=utf-8
"""
Proyecto Polinomio de Taylor.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math
def fact (a):
    if (a==0):
        return 1
    else:
        return a*(fact(a-1))

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
    def polinomio(x):
        f2=f
        polinom=0
        for i in range (n):
            der=derivada(f2)
            if (n==1):
                polinom=f(x0)+der(x0)*(x-x0)
                return polinom
            else:
                if (i>0):
                    polinom=polinom+((der(x0)*(x-x0)**(i+1))/fact(i+1))
                else:
                    polinom=f(x0)+der(x0)*(x-x0)
            f2=der
        return  polinom
        
    return polinomio

if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    f=lambda x: math.sin(x)
    n=0
    x0=0
    prueba=0
    rep="s"
    while (rep =="s" or rep =="S"):
        print ("Polinomio de taylor para aproximar f(x) a valores muy cercanos a x0")
        print ("ingrese el valor de x0")
        x0= float (input())
        print ("ingrese el grado del polinomio")
        n= int (input())
        res=polinomio_taylor(f,x0,n)
        print ("Listo, ingrese el valor de prueba para el polinomio obtenido")
        prueba= float (input())
        print ("valor aproximado: ", res(prueba))
        print ("valor real: ", f(prueba))
        print ("con un error de: ", (f(prueba)-res(prueba))/f(prueba))
        print ("Fin del algoritmo, desea repetir el proceso? (n/s)")
        rep= input ()
        while (rep!= "s" and rep!= "n"):
            print ("ingrese una respuesta correcta (s/n)")
            rep= input ()
    print ("bye.")
    chao=input ()
    pass