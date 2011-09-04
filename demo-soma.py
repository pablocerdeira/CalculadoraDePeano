# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:11:37 2011

@author: pablo
"""

from peano import soma

# OBS:
# O metodo de Peano serve para a soma de quaisquer elementos de um conjunto.
# Entretanto, por sua natureza recursiva, ela e bastante lenta para numeros
# mais altos, como o utilizado na ultima soma de hexadecimais.
# Em meu computador levou 25 minutos.


# Elementos
# Define os elementos basicos a serem utilizados na funcao soma

elementos = ["0","1","2","3","4","5","6","7","8","9"]

# Realiza somas com elementos algebricos
print "Soma com elementos algebricos"
el1, el2 = "0","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "1","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "1","1"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "2","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "5","9"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "76378","983749"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
print " "


# Podemos realizar somas com outras definicoes de elementos, binario por exemplo

elementos = ["0","1"]

# Realiza somas com elementos binarios
print "Soma com elementos binarios"
el1, el2 = "0","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "1","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "1","1"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "11","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "1001","11"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "110001110","10101111"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
print " "


# Podemos realizar somas com hexadecimal (assim como qualquer outro conjunto)

elementos = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

# Realiza somas com elementos binarios
print "Soma com elementos hexadecimais"
el1, el2 = "0","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "1","0"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "A","1"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "AB","DD"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = "AC","D12E"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
# Essa soma a seguir leva cerca de 25 minutos
#el1, el2 = "FFFFD02212","12AFFFDE"
#print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
print " "


# Por que nao somar os naipes do baralho?

# Neste caso precisamos setar os valores com u"" por conta do utf
elementos = [u"♥",u"♦",u"♣",u"♠"]

# Realiza somas com elementos binarios
print "Soma com elementos do naipe do baralho"
el1, el2 = u"♥",u"♥"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = u"♦",u"♥"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = u"♦",u"♦"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = u"♦",u"♠"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
el1, el2 = u"♠",u"♠"
print "Soma %s + %s = %s" % (el1,el2,soma(el1,el2,elementos))
print " "

