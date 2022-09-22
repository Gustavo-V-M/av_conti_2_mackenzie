
def somatorioQuadrados(X):
    soma = 0
    for i in X:
        soma = soma + i**2
    
    return soma

def somatorio(X):
    soma = 0
    for i in X:
        soma = soma + i
    
    return soma

def somatorioProduto(X, Y):
    soma = 0
    for i in range(len(X)):
        soma = soma + X[i]*Y[i]

    return soma


def A(X, Y):

    n = len(X) + 1
    numerador = (n * somatorioProduto(X, Y)) - (somatorio(X) * somatorio(Y))
    denominador = (n * somatorioQuadrados(X)) - (somatorio(X)**2)
        
    return numerador/denominador

def B(X, Y):

    n = len(X) + 1

    numerador = (somatorioQuadrados(X)*somatorio(Y)) - (somatorio(X)*somatorioProduto(X,Y))
    denominador = (n * somatorioQuadrados(X)) - (somatorio(X)**2)

    return numerador/denominador



def regressaoLinear(m):

    x = m[:,0]
    y = m[:,1]

    a = A(x,y)
    b = B(x,y)

    return a, b

# funcoes para o exercicio 2

def factorial(n):
    if n == 0:
        return 1

    return n*factorial(n-1)

def permutacao(n):
    return factorial(n)

def arranjo(n, x):
    return factorial(n)/factorial(n-x)

def combinacao(n, x):
    return factorial(n)/ (factorial(n-x) * factorial(x))

    
# Funções para o exercicio 3

def funcDensidadeBinomial(n, k, p):
    prob_1 = p**k
    prob_2 = (1-p)**(n-k)

    return combinacao(n, k) * prob_1 * prob_2