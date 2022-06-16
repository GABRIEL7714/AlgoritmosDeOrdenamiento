from random import randint
import time 


def insertion_sort(lista):
	inicio = time.time()
	for i in range(len(lista)):
		key = lista[i]
		a = i-1
		while a>=0 and key < lista[a]:
			lista[a+1] = lista[a]
			a = a - 1
		lista[a+1] = key
	final = time.time()
	tiempo = final-inicio
	return tiempo

def bubble_sort(lista):
	n = len(lista)
	inicio = time.time()
	for i in range(n):
		for j in range(n-i-1):
			if lista[j]>lista[j+1]:
				lista[j],lista[j+1] = lista[j+1],lista[j]
	final = time.time()
	tiempo = final-inicio
	return tiempo

lista = []
def crear_lista(n):
	for i in range(n):
		numero = randint(1,100)
		lista.append(numero)



def tiempo_insertionsort():
	n =[100,500,1000,2000,5000,10000,20000,50000]
	for i in range(len(n)):
		crear_lista(n[i])
		print(insertion_sort(lista))


def tiempo_bubblesort():
	n =[100,500,1000,2000,5000,10000,20000,50000]
	for i in range(len(n)):
		crear_lista(n[i])
		print(bubble_sort(lista))




tiempo_insertionsort()
tiempo_bubblesort()







