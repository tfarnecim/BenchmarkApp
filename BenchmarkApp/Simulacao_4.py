import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
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

def BuscaBinaria(lista,item):

    ini = 0
    fim = len(lista)-1
    posicao = -1
    cont = 0

    while(ini<=fim):
        meio = (ini+fim)//2
        cont+=1
        if(lista[meio]==item):
            pos = meio
            break
        elif(lista[meio]>item):
            cont+=1
            fim = meio-1
        else:
            cont+=1
            ini = meio+1

    print("Comparacoes da busca: %d"%(cont))
    return posicao
        

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    BubbleSort(lista)

    fim = time.time()
    print("Tempo final: %f"%(fim))

    time_BS = fim-inicio
    print("%f"%(time_BS))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    posicao = BuscaBinaria(lista, 7500)
    print("Posicao do item eh %d"%(posicao))

    fim = time.time()
    print("Tempo final: %f"%(fim))

    time_BB = fim-inicio
    print("O tempo da busca foi %f"%(time_BB))

    Tempototal = time_BS + time_BB
    print("O tempo total foi %f" %(Tempototal))

if (__name__ == "__main__"):
    main()
