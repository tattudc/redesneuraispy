# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:12:37 2020

@author: TatuEdi
"""
entradas = [-1, 7, 5] #Se entradas[0] = 1 o resultado é positivo se for -1 é negativo
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        #print(entradas[i])
        #print(pesos[i])
        s += e[i] * p[i]
    return s

s = soma(entradas, pesos)

def stepFunc(soma):
    if(soma >=1):
        return 1
    return 0

r = stepFunc(s)