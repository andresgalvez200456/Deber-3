import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""""
def partition(array,f,l):
    #index of smaller element
    i=f-1
    # pivot element
    pivot= array[l]
    for j in range(f,l):
        if array[j]<= pivot:
            # increment index of smaller element
            i = i+1
            array[i],array[j] = array[j],array[i] 
    array[i+1],array[l] = array[l],array[i+1]
    return i+1
def QuickSort(arr,f,l):
    if f < l:
        p = partition(array,f,l)
        QuickSort(array,f, p-1)
        QuickSort(array, p+1,l)

        
# Driver code to test above 
array = [10,63,6,5,9,7] 
n = len(array) 
QuickSort(array,0,n-1) 
print ("Sorted array is:") 
for i in range(n):
    print ("%d" %array[i]),
"""




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


print(quicksort([9,2,6,9,4,6,1,0]))

#complejidad ---> or cada llamada de la funcion, hay un loop O(n) y hay 2 llamadas de la misma funcion para los menores/mayores 
#complejidad ---> 2R * n 
#complejidad 2R * O(n)
#complejidad O(n log n)

#dividir
#cogemos el ultimo elemento de la lista como un pivote 
# ordenamos los elementos del array en sentido que todos los elementos que sean menores al pivote se van a la izquierda y todos los mayores a la derecha

#conquista
#ordenando recursivamente los subarreglos, la izquierda se dividira en su propia (izquierda/derecha) y estas haran lo mismo respectivamente hasta que tengamos una lista izquierda/derecha con longitud 1 que ya van a ser elementos cada vez mayores y menores  

#combinacion
#los elementos ya estarian ordenados solos 

