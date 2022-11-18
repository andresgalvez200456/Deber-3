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
def calcular_tiempo_quick(sequence):
    def quicksort(sequence):
        length = len(sequence) 
        if length <= 1:
            return sequence 
        else:
            pivot = sequence.pop() # retorna y elimina el ultimo elemento 

        items_greater = []
        items_lower = []

        for items in sequence: # O(n)
            if items > pivot:
                items_greater.append(items) 
            else:
                items_lower.append(items)  
    
        return quicksort(items_lower) + [pivot] +  quicksort(items_greater) # 2R 




@timeit1
def calcular_tiempo_merge(nums):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        pivot = int(len(nums) / 2)
        left = merge_sort(nums[0:pivot])
        right = merge_sort(nums[pivot:])
        return merge(left, right)


def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    sorted_list = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            sorted_list.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(right[right_pointer])
            right_pointer += 1
    
    sorted_list.extend(left[left_pointer:])
    sorted_list.extend(right[right_pointer:])
    
    return sorted_list

A = []

for i in range(10000):
    A.append(i)


tiempos_Merge = []
tiempos_Quick = []
z = range(1000)

for i in range(1000):
    random.shuffle(A) # cambia el orden de los valores
    print("Merge")
    calcular_tiempo_merge(A)
    tiempos_Merge.append(calcular_tiempo_merge(A))
    print("Quick_sort")
    calcular_tiempo_quick(A)
    tiempos_Quick.append(calcular_tiempo_quick(A))
    

tiempo = range(1000)
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(tiempo, tiempos_Merge, label='Merge')
ax1.plot(tiempo,tiempos_Quick,  label='Quick')
plt.legend(loc='upper left')
plt.show()



# Merge sort mantiene la misma complejidad de O(n log n) en su peor, mejor o caso promedio 
# Merge sort funciona muy bien con bastantes datos o pocos en cambio quick sort es mas eficiente con datos mas cortos o cuando la distribucion respecto al pivote es casi equitativa porque utiliza menos memoria
# quick sort tiene su peor caso de 0(n^2) cuando un pivote esta a la derecha y la lista a ordenar esta invertida porque tocaria hacer muchas mas particiones en vez de pocas 
# Merge sort es mas rapido cuando se trata de hacer bastantes comparasiones 
# Merge sort requiere 2 subarrays adicionalmente del array original y quick sort depende de la posicion del pivote 