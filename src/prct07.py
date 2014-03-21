#! /usr/bin/python
#!encoding: UTF-8
import moduloaprox

def mostrar(k):
 print l
  
tupla=(10,100,1000,10000,100000,1000000)
l   = []
for valor in tupla:
  apr=moduloaprox.piaprox(valor)
  l = l + [apr]

mostrar(l)
#El número máximo de elementos de la t_upla es 8
#Se producen errores con 9 o mas elementos
#No es posible
#cuando el programador importa un módulo, también crea una versión compilada, o "ya interpretado", de ese módulo, que tiene una extensión "pyc.".