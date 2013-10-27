import matplotlib.pyplot as pl

# Mostrar mas de una representacion en el mismo lienzo 

diagrama1 = pl.figure(1)

# la figura tendra 2 filas y 1 columna y se quiere trazar en la primera
pl.subplot(211)

# para trazar en la segunda 
#pl.subplot(212)

# mostrar por la consola el resultado
pl.show()
