def es_perfecto(n):
  sumatorio = 0
  for i in range(1,n):
    if n % i == 0:
      sumatorio += i
  return sumatorio == n

def tabla_perfectos(m):
  for i in range(1, m+1):
    if es_perfecto(i):
      print i, 'es perfecto'

x = int( raw_input('Introduzca un numero ') )
tabla_perfectos(x)
