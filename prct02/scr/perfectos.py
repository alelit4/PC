def es_perfecto(n):
  sumatorio = 0
  for i in range(1,n):
    if n % i == 0:
      sumatorio += i
  return sumatorio == n

n = 21
print es_perfecto(n)
