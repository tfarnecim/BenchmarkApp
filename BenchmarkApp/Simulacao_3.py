import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def bubble_sort(lista):
    comps = 0
    trocas = 0
    for i in range(len(lista)):
        for c in range(i+1,len(lista)):
            comps+=1
            if(lista[c] < lista[i]):#trocar
                trocas+=1
                aux = lista[i]
                lista[i] = lista[c]
                lista[c] = aux
    print("COMP: %d"%(comps))
    print("TROCAS: %d"%(trocas))

    return lista

def BubbleSort(lista):
    comp = 0
    trocas = 0
    for i in range(len(lista)):
        for j in range(1,len(lista)):
            comp+=1
            if(lista[j] < lista[i]):#trocar
                trocas+=1
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print("Comparacoes da ordenacao: %d"%(comp))
    print("Trocas: %d"%(trocas))

    return lista

def BuscaLinear(lista, item):
    comp = 0
    posicao = -1
    for i in lista:
        posicao+=1
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

    BubbleSort(lista)

    fim = time.time()
    print("Tempo final da Ordenacao: %f"%(fim))
    

    time_BS = fim-inicio
    print("O tempo total da Ordenacao foi: %f"%(time_BS))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    posicao = BuscaLinear(lista, 7500)
    print("Posicao do item eh %d"%(posicao-2))

    fim = time.time()
    print("Tempo final da busca: %f"%(fim))

    time_BL = fim-inicio
    print("O tempo total da busca foi: %f"%(time_BL))

    Tempototal = time_BS + time_BL
    print("O tempo total foi: %f" %(Tempototal))

if (__name__ == "__main__"):
    main()
