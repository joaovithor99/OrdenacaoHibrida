import random

def ordenacao_insercao(lista):
    A = list(lista)
    n = len(A)
    for i in range(1, n):
        chave = A[i]
        j = i - 1
        while j >= 0 and A[j] > chave:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = chave
    return A

def ordenacao_rapida(arr):
    if len(arr) <= 1:
        return arr
    pivo = random.choice(arr)
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    return ordenacao_rapida(menores) + iguais + ordenacao_rapida(maiores)

def ordenacao_hibrida(arr, corte):
    if len(arr) < corte:
        return ordenacao_insercao(arr)
    pivo = random.choice(arr)
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    return ordenacao_hibrida(menores, corte) + iguais + ordenacao_hibrida(maiores, corte)