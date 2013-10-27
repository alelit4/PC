import matplotlib.pyplot as pl
import numpy as np

pl.figure(figsize=(8,6), dpi=80)
pl.subplot(1,1,1)

# A es un vector que hace referencia a 'a' y 'b'
A = np.linspace(0, 3.0, 50, endpoint=True)

# Funciones
X1 = (A*A)** 3
X2 = (A**3)*(A**3)

pl.plot(A,X1,"bo")
pl.plot(A,X2,"r-")


# Incluir un titulo
pl.title('Identidades') 

# Leyenda
pl.legend((r'$ab^3$',r'$a^3 b^3$'), 'upper left', numpoints=2) 

# Poner etiquetas en los ejes 
pl.xlabel('x')
pl.ylabel('y')

# mostrar por la consola el resultado
pl.show()