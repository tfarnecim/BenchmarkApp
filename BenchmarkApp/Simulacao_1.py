import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def bubble_sort(lista):
    comps = 0
    trocas = 0
    for i in range(len(lista)):
        for c in range(i+1,len(lista)):
            comps+=1
            if(lista[c] < lista[i]):
                trocas+=1
                aux = lista[i]
                lista[i] = lista[c]
                lista[c] = aux
    print("COMP: %d"%(comps))
    print("TROCAS: %d"%(trocas))

    return lista

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def pesquisaLinear(lista, elemento_desejado):
    comp = 0
    posicao = -1
    for item in lista:
        posicao = posicao + 1
        comp += 1
        if(item == elemento_desejado):
            break
    print(comp)

    return posicao

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    posicao = pesquisaLinear(lista, 7500)
    print("Posição do item é %d"%(posicao))

    fim = time.time()
    print("Tempo final: %f"%(fim))

    tempoTotal = fim - inicio
    print("O tempo total foi %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
