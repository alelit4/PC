import matplotlib.pyplot as pl

# Lista con los valores de x
x = [ 1, 2, 3, 4, 5]

# Lista con los valores de f(x)
y = [ 1, 4, 9, 16, 25]

# Utilizar la funcion plot para trazar el grafico 
pl.plot(x,y)

# Incluir un titulo
pl.title('Representacion de x frente a y') 

# Poner etiquetas en los ejes 
pl.xlabel('Algunos enteros positivos')
pl.ylabel('Cuadrado de algunos enteros')

# Poner limites a los ejes 
pl.xlim(0.0, 7.0)
pl.ylim(0.0, 30.0)

# mostrar por la consola el resultado
pl.show()

