# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:12:37 2020

@author: TatuEdi
"""
import numpy as np

entradas = np.array([1, 7, 5]) #Se entradas[0] = 1 o resultado é positivo se for -1 é negativo
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):
    return e.dot(p)
#dot é o produto escalar

s = soma(entradas, pesos)

def stepFunc(soma):
    if(soma >=1):
        return 1
    return 0

r = stepFunc(s)