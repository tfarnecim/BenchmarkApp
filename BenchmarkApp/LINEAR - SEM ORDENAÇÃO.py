import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def SemOrdenacao(lista):
    pass

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

    posicao = BuscaLinear(lista, 7500)
    print("Posicao do item eh %d"%(posicao-2))

    fim = time.time()
    print("Tempo final da busca: %f"%(fim))

    time_BL = fim-inicio
    print("O tempo total da busca foi: %f"%(time_BL))

    Tempototal =time_BL
    print("O tempo total foi: %f" %(Tempototal))

if (__name__ == "__main__"):
    main()
