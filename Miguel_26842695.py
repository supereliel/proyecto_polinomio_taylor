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
        #Funcion que devuelve el polinimio de Taylor
        
        pol= lambda: 0 #Variable donde se almacena el polinomio

        nueva_f=f 

        """nueva_ f: variable que va a contener las derivadas que vayan surgiendo
        a medida que se itere, se inicializa siendo igual a la funcion dada
        
        i: contador que almacena el numero de iteraciones
        """

        def pol_taylor_recursivo(f,x0,n,nueva_f,i,pol):
            #Funcion recursiva que realiza los calculos para obtener el polinomio

            if i==n: #Condicion de parada (Se alcanza el numero maximo de grado)

                return pol
                
            elif i==0: #Primera iteracion

                pol=f(0) #Se calcula f(x0)
                return pol_taylor_recursivo(f,x0,n,nueva_f,i+1,pol)

            else: #Iteraciones siguentes

                derv_f=derivada(nueva_f)
                nueva_f=derv_f
                pol=pol+derv_f(x0)*(x-x0)**i/math.factorial(i) #Se calcula el polinomio
                return pol_taylor_recursivo(f,x0,n,nueva_f,i+1,pol)

        # Se retorna la funcion que calculo el polinomio
        return pol_taylor_recursivo (f,x0,n,nueva_f,0,pol) 
    
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.

    f= lambda x: math.sin(x)

    j= lambda x: math.exp(2*x)

    poli=polinomio_taylor(j,0,2)

    print("Valor Aproximado", poli(0.3))