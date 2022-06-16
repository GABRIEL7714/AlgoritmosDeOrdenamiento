def insertion_sort(lista):
	for i in range(len(lista)):
		key = lista[i]
		a = i-1
		while a>=0 and key < lista[a]:
			lista[a+1] = lista[a]
			a = a - 1

		lista[a+1] = key

	return lista 


def bubble_sort(lista):
	n = len(lista)
	for i in range(n):
		for j in range(n-i-1):
			if lista[j]>lista[j+1]:
				lista[j],lista[j+1] = lista[j+1],lista[j]

	return lista


#LISTA
lista = [6,7,9,4,0,5,1,56,75,23]
menu = """
1_Insertio_sort
2_Bubble_sort
"""
opcion = input("Ingrese un opcion: ")
if opcion == "1":
	print(insertion_sort(lista))

if opcion == "2":
	print(bubble_sort(lista))