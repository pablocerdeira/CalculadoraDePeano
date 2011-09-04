# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 19:30:24 2011

@author: pablo
"""

from peano import s


# Elementos
# Define os elementos básicos a serem utilizados na funcao s

# Eles podem ser os caracteres algebricos...
elementos = ["0","1","2","3","4","5","6","7","8","9"]

print "Testa o funcionamento da funcao s com algebricos decimais"
print "O elemento seguinte a %s é %s" % ("0",s("0",elementos))
print "O elemento seguinte a %s é %s" % ("1",s("1",elementos))
print "O elemento seguinte a %s é %s" % ("2",s("2",elementos))
print "O elemento seguinte a %s é %s" % ("3",s("3",elementos))
print "O elemento seguinte a %s é %s" % ("9",s("9",elementos))
print "O elemento seguinte a %s é %s" % ("14",s("14",elementos))
print "O elemento seguinte a %s é %s" % ("19",s("19",elementos))
print "O elemento seguinte a %s é %s" % ("99999",s("99999",elementos))
print " "


# ...os elementos podem ser binarios ...
elementos = ["0","1"]

print "Testa o funcionamento da funcao s com binários"
print "O elemento seguinte a %s é %s" % ("0",s("0",elementos))
print "O elemento seguinte a %s é %s" % ("1",s("1",elementos))
print "O elemento seguinte a %s é %s" % ("10",s("10",elementos))
print "O elemento seguinte a %s é %s" % ("11",s("11",elementos))
print "O elemento seguinte a %s é %s" % ("100",s("100",elementos))
print "O elemento seguinte a %s é %s" % ("101",s("101",elementos))
print "O elemento seguinte a %s é %s" % ("110",s("110",elementos))
print "O elemento seguinte a %s é %s" % ("111",s("111",elementos))
print " "

# ... os elementos podem ser hexadecimais ...
elementos = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

print "Testa o funcionamento da funcao s com hexadecimal"
print "O elemento seguinte a %s é %s" % ("0",s("0",elementos))
print "O elemento seguinte a %s é %s" % ("1",s("1",elementos))
print "O elemento seguinte a %s é %s" % ("9",s("9",elementos))
print "O elemento seguinte a %s é %s" % ("A",s("A",elementos))
print "O elemento seguinte a %s é %s" % ("F",s("F",elementos))
print "O elemento seguinte a %s é %s" % ("AA",s("AA",elementos))
print "O elemento seguinte a %s é %s" % ("FF",s("FF",elementos))
print "O elemento seguinte a %s é %s" % ("FFFFFF",s("FFFFFF",elementos))
print " "

# ... os elementos podem ser só letras ...
elementos = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

print "Testa o funcionamento da funcao s com letras"
print "O elemento seguinte a %s é %s" % ("A",s("A",elementos))
print "O elemento seguinte a %s é %s" % ("B",s("B",elementos))
print "O elemento seguinte a %s é %s" % ("C",s("C",elementos))
print "O elemento seguinte a %s é %s" % ("M",s("M",elementos))
print "O elemento seguinte a %s é %s" % ("Z",s("Z",elementos))
print "O elemento seguinte a %s é %s" % ("ZD",s("ZD",elementos))
print "O elemento seguinte a %s é %s" % ("RST",s("RST",elementos))
print "O elemento seguinte a %s é %s" % ("ZZZZ",s("ZZZZ",elementos))
print " "

