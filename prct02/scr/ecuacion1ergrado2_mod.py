#!/usr/bin/env python
# -*- coding: utf-8 -*-

#a * x + b = 0
a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if a != 0:
  x = -b/a
  print 'Solucion: ', x
if a == 0:
  if b == 0:
  	print 'La ecuación tiene infinitas soluciones.'
  else:
  	print 'La ecuación no tiene solución.'
