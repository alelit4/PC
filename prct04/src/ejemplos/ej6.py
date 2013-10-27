import matplotlib.pyplot as pl

# Anadir leyendas 

# Lista con los valores de x e y de una funcion
x0 = [ 1, 2, 3, 4, 5]
y0 = [ 1, 4, 9, 16, 25]

# Lista con los valores de x e y de otra funcion
x1 = [ 1, 2, 4, 6, 8]
y1 = [ 2, 4, 8, 12, 16]

# Trazar ambas funiones
plot0 = pl.plot(x0,y0,'r--')
plot1 = pl.plot(x1,y1,'bo')

# Incluir un titulo
pl.title('Representacion de x frente a y') 

# Poner etiquetas en los ejes 
pl.xlabel('Algunos enteros positivos')
pl.ylabel('Cuadrado y doble de algunos enteros')

# Poner limites a los ejes 
pl.xlim(0.0, 9.0)
pl.ylim(0.0, 30.0)

# Poner una leyenda
# localizacion:
#  'best'
#  'upper right'
#  'upper left'
#  'lower left'
#  'lower right'
#  'right'
#  'center left'
#  'center right'
#  'lower center'
#  'upper center'
#  'center'
# numpoints: numero de puntos para una linea

# pl.legend([plot0, plot1], ('cuadrado','doble'), 'best', numpoints=2) 
pl.legend(('cuadrado','doble'), 'best', numpoints=2) 

# mostrar por la consola el resultado
pl.show()
