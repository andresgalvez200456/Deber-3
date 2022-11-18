import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
    
    def set_next_node(self, next_node):
        self.next_node = next_node


        
class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

class Singly_linked_list(Singly_linked_list):
    def insert_head(self, new_node):
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null 
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def insert_tail(self, new_node):
        # insert to the tail
        # A -> B -> null
        # A -> B -> R -> null 
        node = self.head_node
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(new_node)
        
    def insert_middle(self, new_node, value):
        # insert in the middle
        # A -> B -> C -> null
        # A -> B -> R -> C -> null
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node) 



global sorted_list
sorted_list = Singly_linked_list()

def compare(node_A, node_B):    #complejidad es R x O(1)
                                # R porque se llama una vez a la la funcion Compare() por cada numero de nodos que tenemos dentro de 2 listas enlazadas
                                # O(1) porque siempre hago una asignacion y un insertar en la cabeza dentro de una tercera lista que es la ordenada 
                                #por lo tanto quiere decir que la complejidad depende de cuantos numeros contenga las linked list antes que la complejidad dentro de la funcion porque O(1) es trivial
                                 
        if(node_A == None):
            sorted_list.insert_head(node_B)
            return node_B
        if(node_B == None):
            sorted_list.insert_head(node_A)
            return node_A

        if(node_A.val < node_B.val): # comparar los valores de cada nodo 
            node_A.next_node = compare(node_A.next_node, node_B) # 
            sorted_list.insert_head(node_A) #O(1)
            return node_A
        else:
            node_B.next_node = compare(node_A, node_B.next_node)
            sorted_list.insert_head(node_B)
            return node_B


"""""
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node) 
"""


"""
def merge(lista_A, lista_B, sorted_linked_list):
    node = lista_A.head_node
    while node:
        if(lista_A.head_node < lista_B.head_node):
            sorted_linked_list.insert_head(lista_A.head_node)
            node = node.next_node
        else:
            sorted_linked_list.insert_head(lista_B.head_node)
            node = node.next_node
"""

if __name__ == '__main__':
    m1 = Node(1)
    m2 = Node(3)
    m3 = Node(5)
    m4 = Node(7)

    m1.set_next_node(m2)
    m2.set_next_node(m3)
    m3.set_next_node(m4)

    list_A = Singly_linked_list(m1)

    list_A.list_traversed()

    print(" ")

    n1 = Node(2)
    n2 = Node(4)
    n3 = Node(6)

    n1.set_next_node(n2)
    n2.set_next_node(n3)

    list_B = Singly_linked_list(n1)

    list_B.list_traversed()

    print(" ")


    compare(m1,n1)

    sorted_list.list_traversed()
    
