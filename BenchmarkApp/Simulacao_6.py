import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.

def BuscaBinaria(lista,item):

    ini = 0
    fim = len(lista)-1
    posicao = -1
    cont = 0

    while(ini<=fim):
        meio = (ini+fim)//2
        cont+=1
        if(lista[meio]==item):
            posicao = meio
            break
        elif(lista[meio]>item):
            cont+=1
            fim = meio-1
        else:
            cont+=1
            ini = meio+1

    print("Comparacao da busca: %d"%(cont))
    return posicao
        

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

    posicao = BuscaBinaria(lista, 7500)
    print("Posicao do item eh %d"%(posicao))

    fim = time.time()
    print("Tempo final da busca: %f"%(fim))

    time_BB = fim-inicio
    print("O tempo total da busca foi: %f"%(time_BB))

    Tempototal = time_MS + time_BB
    print("O tempo total foi: %f" %(Tempototal))

if (__name__ == "__main__"):
    main()
