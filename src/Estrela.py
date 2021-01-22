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

# Dentro do diretório digite python3 Estrela.py ou python Estrela.py (caso a versão 3 seja padrão).

class Begin():
    def __init__(self):
        # LISTA REPRESENTANDO O NO USADO.
        no = []

        # ARRAY AUXILIAR PARA MARCAÇÃO DE ESTAÇÕES JÁ OU NÃO VISITADAS.
        visitados = [0]*14

        resposta = []

        # PARA SOMAR A QUANTIDADE DE ESTAÇÕES VISITADAS DESCONSIDERANDO A INICIAL.
        trocasDeEstacao = 0
        
        # PARA SOMA DOS CUSTOS. 
        km = 0

        # HEURISTICA LINHA RETA
        H = Heuristica['H'] 

        # TABELA DE CUSTO, REPRESENTANDO TAMBEM A COR DA LINHA É FEITA A LIGAÇÃO
        C = Custo['C']

        # ARRAY COM NOME DAS ESTAÇÕES DO MAPA
        E = Estacoes['E']
        
        #	PEGAR ESTAÇÃO INICIAL.
        def partida():
            print("Informe sua Estação de Origem:")
            for i in range(0, len(E)):
                print("{} - {}".format(i+1, E[i]), end="  ", flush=True)
            print("\nSua escolha:", end=" ")    
            p = int(input())-1
            if(p < 0 or p > 14):
                print("Por favor, selecione o número de uma das estações abaixo:")
                partida()
            return p

        #	PEGAR DESTINO FINAL.
        def chegada():
            print("Informe sua Estação de Destino:")
            for i in range(0, len(E)):
                print("{} - {}".format(i+1, E[i]), end="  ", flush=True)
            print("\nSua escolha:", end=" ")       
            c = int(input())-1
            return c

        def converterParaTempo(x):
            mins = x*2
            return mins

        def definir_Estacao(E):
            #Linha Azul.
            if E == None:
                print("E1<->E2", end="", flush=True)
            elif E == 10: 
                print("E1<->E2", end="", flush=True)
            elif E == 8.5:
                print("E2<->E3", end="", flush=True)
            elif E == 6.3:
                print("E3<->E4", end="", flush=True)
            elif E == 13:
                print("E4<->E5", end="", flush=True)
            elif E == 3:
                print("E5<->E6", end="", flush=True)

            #Linha Amarela.            
            elif E == 10.1:
                print("E2<->E9", end="", flush=True)
            elif E == 3.5: 
                print("E2<->E10", end="", flush=True)
            elif E == 2.4:
                print("E5<->E7", end="", flush=True)
            elif E == 30:
                print("E5<->E8", end="", flush=True)
            elif E == 9.6:
                print("E8<->E9", end="", flush=True)

            #Linha Verde.         
            elif E == 5.1:
                print("E13<->E14", end="", flush=True)
            elif E == 6.4:
                print("E8<->E12", end="", flush=True)
            elif E == 12.8:
                print("E4<->E13", end="", flush=True)
            elif E == 15.3:
                print("E4<->E8", end="", flush=True)
            
            #Linha Vermelha.
            elif E == 9.4:
                print("E3<->E9", end="", flush=True)   
            elif E == 18.7:
                print("E3<->E13", end="", flush=True) 
            elif E == 12.2:
                print("E9<->E11", end="", flush=True)   

        def printar_no():
            for i in range(0, len(no)):
                if(visitados[no[i][2]] == 0):
                    print(" | ", end="", flush=True)
                    definir_Estacao(no[i][4])

        def caminho(a):
            while a[3][2] != -1:
                resposta.append(a[3][2])
                a = a[3] 

        def sucessores_de(a):
            antecessor = []
            for i in range (0, len(E)):
                if(C[a[2]][i] != 0 and visitados[a[2]] == 0):
                    #	CALCULAR O G DESSE SUCESSOR
                    g = converterParaTempo(a[3][1] + H[a[2]][i])
                    #	CALCULAR H DESSE SUCESSOR
                    h = converterParaTempo(H[i][pontoChegada])
                    #	ANTECESSOR DO SUCESSOR (DE QUE ESTAÇÃO ESSE TREM CHEGOU EM i)
                    antecessor = a
                    #	COR DA LINHA EM QUE EST
                    linha = C[a[2]][i]
                    #	ADICIONAR O NÓ NO NOVO SUCESSOR
                    s = [h+g, g, i, antecessor, linha]
                    no.append(s)
            print("\nExpansão dos Nós:", end=" ", flush=True)        
            definir_Estacao(antecessor[4])      
            visitados[a[2]] = 1

        def estrela():
            k = 0
            while k > -1:	
                for i in range(0, len(no)):
                    if(visitados[no[i][2]] == 0):
                        break
                if(no[i][2] == pontoChegada):
                    visitados[no[i][2]] = 1
                    resposta.append(no[i][2])
                    caminho(no[i])
                    break
                sucessores_de(no[i])
                no.sort(key=lambda no: no[0])
                printar_no()
                k += 1

        pontoPartida = partida()
        pontoChegada = chegada()

        print("\nESTADO INICIAL: {}".format(E[pontoPartida]))
        print("ESTADO   FINAL: {}".format(E[pontoChegada]))
        print("\n!!!VALE RESSALTAR QUE OS NÓS ESTÃO PARA AMBOS SENTIDOS!!!\n")

        V = [0, 0, -1, -1, -1]

        a = [converterParaTempo(0 + H[pontoPartida][pontoChegada]), 0, pontoPartida, V, None]
        no.append(a)
        estrela()
        final = resposta[::-1] 
        
        print("\n\nMelhor caminho entre: E{} -> E{}".format(pontoPartida + 1, pontoChegada + 1))
        for i in range (0, len(final)):
            if i == 0:
                print("Saindo da Estação:", end="")
                print("".format(definir_Estacao(C[final[i]][final[i+1]])))
                km += (H[final[i]][final[i+1]] + C[final[i]][final[i+1]])

            elif i == len(final)-1:
                print("Chegou na estação: E{}".format(final[i]+1))
            else:
                km += H[final[i]][final[i+1]] + C[final[i]][final[i+1]]
                if C[final[i-1]][final[i]] != C[final[i]][final[i+1]]:
                    print("Houve uma troca de linha entre:", end=" ")
                    trocasDeEstacao += 1
                print("".format(definir_Estacao(C[final[i]][final[i+1]])))

        print("Percorridos: {} km com {} troca(s) de Estação\n".format(km, trocasDeEstacao + 1))

try: 
    if os.path.exists("Heuristica.json") and os.path.exists("Custo.json") and os.path.exists("Estacoes.json"):
        f1 = open("Heuristica.json")
        f2 = open("Custo.json")
        f3 = open("Estacoes.json")

        Heuristica = json.load(f1)
        Estacoes = json.load(f3)
        Custo = json.load(f2)

        f1.close
        f2.close
        f3.close
    else:
        print('Arquivos passados por parâmetro não encontrados.\n')
        sys.exit(0)

    start = Begin()    

    while True:
        print("Deseja Continuar? Aperte 1-SIM e 2-NÃO")
        x = int(input())

        if x == 1:
            start.__init__()
        else: 
            sys.exit(0)    

except (EOFError, KeyboardInterrupt) as e:  #ctrl + d, ctrl + c.  
    sys.exit(0)  

  