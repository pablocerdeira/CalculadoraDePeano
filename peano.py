# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 19:30:24 2011

@author: pablo
"""


# Funcao de sucessao
def s(elemento,elementos,esquerda=""):

    # As operacoes matematicas aqui utilizadas, como +1 e -1
    # nao sao utilizadas sobre os elementos, mas apenas para
    # movimentacao na lista de elementos.

    # Pega o caracter mais a direita e chama s recursivamente
    if len(elemento) > 1:
        return s(elemento[-1],elementos,elemento[:-1])
    else:
        try:
            pos = elementos.index(elemento)
        except ValueError:
            return "O valor %s nao pertencente aos elementos." % str(elemento)
            
        if pos >= len(elementos)-1:
            if esquerda == "":
                esquerda = elementos[0]
            maior = s(esquerda,elementos)
            return maior + elementos[0]
        else:
            return esquerda + elementos[pos+1]


def soma(elemento1,elemento2,elementos):
    # a + 0 = a
    # a + s(b) = s(a + b)
    
    # seta elemento como primeiro elemento da lista de elementos
    elemento = elementos[0]
    # loop para determinar quantos sucessores a partir do primeiro sao
    # necessarios para se chegar ate o elemento2 da soma
    while elemento2 != elemento:
        elemento = s(elemento,elementos)
        # seleciona o sucessor de elemento1 tantas vezes quantas forem
        # necessarias para que o elemento seja igual a elemento2
        elemento1 = s(elemento1,elementos)
    return elemento1
    
    
def multiplicacao(elemento1,elemento2,elementos):
    # a * 0 = 0
    # a + s(b) = a + (a * b)

    # seta elemento como primeiro elemento da lista de elementos
    elemento0 = elementos[0]
    elemento_final = elemento1

    # Se algum dos elementos for o primeiro dos elementos, então retornar ele mesmo
    if elemento1 == elemento0 or elemento2 == elemento0:
        return elemento0
    
    # loop para determinar quantos sucessores a partir do primeiro sao
    # precisos para se chegar ate o elemento2 da soma
    while elemento2 != s(elemento0,elementos):
        elemento0 = s(elemento0,elementos)
        # seleciona o sucessor de elemento1 tantas vezes quantas forem
        # necessarias para que o elemento seja igual a elemento2
        elemento_final = soma(elemento_final,elemento1,elementos)
    return elemento_final

