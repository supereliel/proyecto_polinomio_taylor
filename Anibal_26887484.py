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
    p:Polinomio
    d_Actual:Derivada actual
    """
    def polinomio(x):
        i=1
        p=f(x0)     #Comienzo del polinomio 
        while (i!=n+1):
            if (i==1):
                d_Actual=derivada(f)    #Se asigna la primera derivada
                p+=d_Actual(x0) * (x-x0)    #Se agrega al polinomio la primera derivada
            else:
                d_Actual=derivada(d_Actual) #Se calculan todas las derivadas siguientes a la primera
                p+=( d_Actual(x0) * (x-x0)**i ) / math.factorial(i) #Se agregan al polinomio las demas iteraciones
            i+=1      
        return p
    return polinomio
f1=lambda x: math.sin(x)    #Ejercicio realizado en clase
f2=lambda x: math.exp(2*x)  #Funcion de prueba 

def prueba(f,x,x0,n):  #Funcion para probar los ejercicios
    poli=polinomio_taylor(f,x0,n)
    print("Valor Aproximado: ",poli(x))
    print("      Valor Real: ",f(x))
    print("  Error Relativo: ", f(x)-poli(x))

if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    prueba(f1,0.3,0,4)
