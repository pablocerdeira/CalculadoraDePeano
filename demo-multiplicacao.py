# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:11:37 2011

@author: pablo
"""

from peano import multiplicacao


# Elementos
# Define os elementos basicos a serem utilizados na funcao soma

elementos = ["0","1","2","3","4","5","6","7","8","9"]

# Realiza multiplicacoes com elementos algebricos
print "Multiplicacao com elementos algebricos"
el1, el2 = "0","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "1","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "1","1"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "2","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "5","9"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "76","98"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "667","121"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
print " "


# Podemos realizar multiplicacoes com outras definicoes de elementos, binario por exemplo

elementos = ["0","1"]

# Realiza multiplicacoes com elementos binarios
print "Multiplicacao com elementos binarios"
el1, el2 = "0","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "1","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "1","1"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "11","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "1001","11"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "110001110","10101111"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
print " "


# Podemos realizar multiplicacoes com hexadecimal (assim como qualquer outro conjunto)

elementos = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

# Realiza multiplicacoes com elementos binarios
print "Multiplicacao com elementos hexadecimais"
el1, el2 = "0","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "1","0"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "A","1"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "AB","DD"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "AC","D12E"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = "FF12","AFDE"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
print " "


# Por que nao multiplicar os naipes do baralho?

# Neste caso precisamos setar os valores com u"" por conta do utf
elementos = [u"♥",u"♦",u"♣",u"♠"]

# Realiza multiplicacoes com elementos binarios
print "Multiplicacao com elementos do naipe do baralho"
el1, el2 = u"♥",u"♥"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = u"♦",u"♥"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = u"♦",u"♦"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = u"♦",u"♠"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
el1, el2 = u"♠",u"♠"
print "Multiplicacao %s * %s = %s" % (el1,el2,multiplicacao(el1,el2,elementos))
print " "

