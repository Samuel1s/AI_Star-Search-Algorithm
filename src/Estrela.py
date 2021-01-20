#*******************************************************************************
#*                      Melhor caminho entre as estações                       *
#*-----------------------------------------------------------------------------*
#* @AUTHOR: Samuel Filipe dos Santos.                                          *
#* @TEACHER: Rogério Martins Gomes.                                            *
#* @LANGUAGE: Python                                                           *
#* @DISCIPLINE: Inteligência Artificial                                        *
#* @CODING: UTF-8                                                              *
#* @DATE: 22 de Janeiro de 2021                                                *
#*******************************************************************************

import json
import sys
import os

class Begin():
    def __init__(self):
        # LISTA REPRESENTANDO A FRONTEIRA USADA PARA A BUSCA DO A*
        fronteira = []

        # ARRAY AUXILIAR PARA MARCAÇÃO DE ESTAÇÕES JÁ OU NÃO VISITADAS
        visitados = [0]*14

        resposta = []

        trocasDeEstacao = 0
        
        km = 0
        # TABELA DE DISTANCIAS EM LINHA RETA
        H = Heuristica['H'] 

        # TABELA DE LIGAÇÕES, REPRESENTANDO TAMBEM A COR DA LINHA É FEITA A LIGAÇÃO
        L = Custo['L']
        # ARRAY COM NOME DAS ESTAÇÕES DO MAPA
        E = Estacoes['E']
        

        #	PEGAR ESTAÇÃO INICIAL QUE O PASSAGEIRO SE ENCONTRA
        def partida():
            print("Informe sua Estação:")
            for i in range(0, len(E)):
                print("{} - {}".format(i+1, E[i]))
            p = int(input())-1
            if(p < 0 or p > 14):
                print("Por favor, selecione o número de uma das estações abaixo:")
                partida()
            return p

        #	PEGAR DESTINO FINAL DO PASSAGEIRO
        def chegada():
            print("Informe seu Destino:")
            for i in range(0, len(E)):
                print("{} - {}".format(i+1, E[i]))
            c = int(input())-1
            return c

        def converterParaTempo(x):
            mins = x*2
            return mins


        def printar_fronteira():
            for i in range(0, len(fronteira)):
                print("FRONTEIRA:")
                if(visitados[fronteira[i][2]] == 0):
                    print(fronteira[i])

        def caminho(a):
            while a[3][2] != -1:
                resposta.append(a[3][2])
                a = a[3] 

        def sucessores_de(a):
            for i in range (0, len(E)):
                if(L[a[2]][i] != 0 and visitados[a[2]] == 0):
                    #	CALCULAR O G DESSE SUCESSOR
                    g = converterParaTempo(a[3][1] + H[a[2]][i])
                    #	CALCULAR H DESSE SUCESSOR
                    h = converterParaTempo(H[i][pontoChegada])
                    #	PAI DO SUCESSOR (DE QUE ESTAÇÃO ESSE TREM CHEGOU EM i)
                    pai = a
                    #	COR DA LINHA
                    linha = L[a[2]][i]
                    if(a[4] != linha):
                        h += 0	#	ACRESCIMO DOS 4 MINUTOS NA TROCA DE LINHA
                    #	ADICIONAR NA FRONTEIRA NOVO SUCESSOR
                    s = [h+g, g, i, pai, linha]
                    fronteira.append(s)
            
            visitados[a[2]] = 1

        def estrela():
            k = 0
            while k > -1:	
                # AINDA NÃO CHEGAMOS...
                for i in range(0, len(fronteira)):
                    if(visitados[fronteira[i][2]] == 0):
                        break
                if(fronteira[i][2] == pontoChegada):
                    visitados[fronteira[i][2]] = 1
                    resposta.append(fronteira[i][2])
                    caminho(fronteira[i])
                    break
                sucessores_de(fronteira[i])
                fronteira.sort(key=lambda fronteira: fronteira[0])
                printar_fronteira()
                k += 1

        # MAIN

        pontoPartida = partida()
        pontoChegada = chegada()

        print("ESTADO INICIAL: {}".format(E[pontoPartida]))
        print("ESTADO   FINAL: {}".format(E[pontoChegada]))

        V = [0, 0, -1, -1, -1]

        # E = [f, g, indiceEstacao, pai, corDaLinha]
        a = [converterParaTempo(0 + H[pontoPartida][pontoChegada]), 0, pontoPartida, V, None]

        fronteira.append(a)

        estrela()

        final = resposta[::-1] 

        print("\n\nMelhor Caminho: E{} -> E{}".format(pontoPartida+1, pontoChegada+1))
        for i in range (0, len(final)):
            if i == 0:
                print("Saindo da Estação: [E{} : {}]\n".format(final[i]+1, E[final[i]]))
                km += (H[final[i]][final[i+1]])
            elif i == len(final)-1:
                print("...Chegando na Estação: [E{} : {}]\n".format(final[i]+1, E[final[i]]))
            else:
                km += H[final[i]][final[i+1]]
                if L[final[i-1]][final[i]] != L[final[i]][final[i+1]]:
                    print(">> TROCA DE ESTAÇÃO! <<")
                    trocasDeEstacao += 1
                print("- Passando por [E{} : {}]...\n".format(final[i]+1, E[final[i]]))

        print("Percorridos: {} km com {} troca(s) de Estação".format(km, trocasDeEstacao))

try: 
    if os.path.exists("Heuristica.json") and os.path.exists("Nos.json") and os.path.exists("Estacoes.json"):
        f1 = open("Heuristica.json")
        f2 = open("Nos.json")
        f3 = open("Estacoes.json")

        Heuristica = json.load(f1)
        Estacoes = json.load(f3)
        Custo = json.load(f2)

        f1.close
        f2.close
        f3.close
    else:
        print('Arquivos passado por parâmetro não encontrado.\n')
        sys.exit(0)

    start = Begin()    

    while True:
        start.__init__()

except (EOFError, KeyboardInterrupt) as e:  #ctrl + d, ctrl + c.  
    sys.exit(0)  

  