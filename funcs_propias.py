import numpy as np
    

def somatorioQuadrados(X):
    soma = 0
    for i in X:
        soma = soma + i**2
    
    return soma

def somatorio(X):
    soma = 0
    for i in X:
        soma = soma + i**2
    
    return soma

def somatorioProduto(X, Y):
    soma = 0
    for i in range(len(X)):
        soma = soma + X[i]*Y[i]

    return soma

def A(X, Y):


    n = len(X)
    numerador = (n * somatorioProduto(X, Y)) - (somatorio(X) * somatorio(Y))
    denominador = (n * somatorioQuadrados(X)) - (somatorio(X)**2)
        
    return numerador/denominador

def B(X, Y):

    n = len(X)

    numerador = (somatorioQuadrados(X)*somatorio(Y)) - (somatorio(X)*somatorioProduto(X,Y))
    denominador = (n * somatorioQuadrados(X)) - (somatorio(X)**2)

    return numerador/denominador

def regressaoLinear(m):

    x = m[:,0]
    y = m[:,1]

    a = A(x,y)
    b = B(x,y)

    return a, b

    

    