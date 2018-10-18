import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.


def MergeSort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        cont1 = lista[:meio]
        cont2 = lista[meio:]

        MergeSort(cont1)
        MergeSort(cont2)

        i = 0
        j = 0
        k = 0
        while i < len(cont1) and j < len(cont2):
            if cont1[i] < cont2[j]:
                lista[k]=cont1[i]
                i=i+1
            else:
                lista[k]=cont2[j]
                j=j+1
            k=k+1

        while i < len(cont1):
            lista[k] = cont1[i]
            i=i+1
            k=k+1

        while j < len(cont2):
            lista[k] = cont2[j]
            j=j+1
            k=k+1


def BuscaLinear(lista, item):
    comp = 0
    posicao = -1
    for i in lista:
        posicao = posicao + 1
        comp += 1
        if(i == item):
            break
    print("comparacoes da busca: %d"%(comp))

    return posicao

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

    inicio = time.time()
    print("Tempo inicial da Ordenacao: %f"%(inicio))

    MergeSort(lista)

    fim = time.time()
    print("Tempo final da Ordenacao: %f"%(fim))
    

    time_MS = fim-inicio
    print("O tempo total da Ordenacao foi: %f"%(time_MS))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    posicao = BuscaLinear(lista, 7500)
    print("Posicao do item eh %d"%(posicao))

    fim = time.time()
    print("Tempo final da busca: %f"%(fim))

    time_BL = fim-inicio
    print("O tempo total da busca foi: %f"%(time_BL))

    Tempototal = time_MS + time_BL
    print("O tempo total foi: %f" %(Tempototal))

if (__name__ == "__main__"):
    main()
