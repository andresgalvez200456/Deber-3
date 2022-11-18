import math
import random
import time
from functools import wraps
import matplotlib.pyplot as plt


list_time = []
def timeit1(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time  
        list_time.append(total_time)      
        print(f' Took {total_time:.10f} seconds')
        return total_time 
    return timeit_wrapper


@timeit1
def calcular_tiempo_factorial(a):
    def factorial(a): # factorial recursividad 
        if(a==0):                   #constante
            f = 1;                  #constante
        else:                       #constante
            f = a*factorial(a-1)    #R se ejecuta n veces    , si (a) es 5, factorial se ejecuta 5 veces y las demas de lineas de condigo son constantes  
        return f                    #constante

#complejidad O(n)      
#5 * 4 * 3 * 2 * 1
# 4 * 3 * 2 * 1
#  3 * 2 * 1
#   2 * 1 
#    1 * 1
#     0 --> CASO BASE 
#  si ingreso 5, el codigo se ejectura x5 veces

@timeit1
def calcular_tiempo_factorialCache(a):
    cache = {}
    def factorialCache(a):
        if(a in cache.keys()): # si el resultado a existe, no lo volvemos a calcular sino que ya lo tenemos guardado 
            return cache[a]
        if (a == 0):
            f = 1
        else: 
            if(a == 1):
                f = 1
            else:
                f = a*factorialCache(a-1)
        cache[a] = f
        return f

# complejidad constante  

tiempos_recursividad = []
tiempos_cache = []

for i in range(10000):
    print(" base --> ", i)
    print(" ")
    print(calcular_tiempo_factorial(i) )
    tiempos_recursividad.append(calcular_tiempo_factorial(i))
    print(" ")
    print(calcular_tiempo_factorialCache(i) )
    tiempos_cache.append(calcular_tiempo_factorialCache(i))

#print(factorialCache(3))




tiempo = range(10000)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(tiempo, tiempos_recursividad, label='recursividad')
ax1.plot(tiempo,tiempos_cache,  label='memoization')
plt.legend(loc='upper left')
plt.show()


#la diferenciacion es que forma recursiva necesita volver a calcular el resultado anterior a la recursion para sacar poder calcular el nuevo velor mientras que la forma memoization en cambio es tiene una memoria aparte donde se guardan los valores que se estan calculando para ahorrar complejidad de codigo y acceder a ellos rapidamente 