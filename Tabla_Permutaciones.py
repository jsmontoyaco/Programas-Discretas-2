## Juan Sebastian  Montoya Combita
##este programa se basa en el algoritmo de Pandit

def get_indice_medio(A):
    indice = len(A) - 1
    while indice > 0:
        if A[indice] < A[indice - 1]:
            indice -= 1
        else:
            break
    return indice - 1
 
def get_cambiar_indice(A, indice_medio):
    indice_cambio = len(A) - 1
    while indice_cambio >= indice_medio:
        if A[indice_cambio] > A[indice_medio]:
            break
        else:
            indice_cambio -= 1
    return indice_cambio
 
def intercambio(A, indice_medio, indice_cambio):
    A[indice_medio], A[indice_cambio] = (A[indice_cambio], A[indice_medio])
 
 

def regreso(A, inicio):
    izq = inicio
    der = len(A) - 1
    while izq < der:
        intercambio(A, izq, der)
        izq += 1
        der -= 1
 
def siguiente_permutacion(A):
    indice_medio = get_indice_medio(A)
    # the Array is sorted in descreased order
    if indice_medio == -1:
        regreso(A, 0)
    else:
        cambiar_indice = get_cambiar_indice(A, indice_medio)
        intercambio(A, indice_medio, cambiar_indice)
        regreso(A, indice_medio + 1)
 
 
A = [1,2,3,4,5]

for i in range(120): ##donde el elemento del rango es el número de combinaciones posibles
    siguiente_permutacion(A)
    print (A)
    