import matplotlib.pyplot as pl

# Lista con los valores de x
x = [ 1, 2, 3, 4, 5]

# Lista con los valores de f(x)
y = [ 1, 4, 9, 16, 25]

# Utilizar la funcion plot para trazar el grafico 
# Hacer un trazado disperso
# color
# b - blue
# g - green
# r - red
# c - cyan
# m - magenta
# y - yellow
# k - black
# w - white
# marcador
# o - circle
# s - square
# p - pentagon
# * - star 
# h - hexagon
# + - plus
# d - diamond
pl.plot(x,y,'bo')

# mostrar por la consola el resultado
pl.show()
