import random

# definindo tamanho da matriz
# tamanho_matriz = int(input("Defina o tamanho da matriz quadrada: "))
# tamanho_linhas_matriz = tamanho_matriz
# tamanho_colunas_matriz = tamanho_matriz
tamanho_matriz = 8 # forçando o tamanho da matriz
tamanho_linhas_matriz = 8 # forçando o tamanho das linhas da matriz
tamanho_colunas_matriz = 8 # forçando o tamanho das colunas da matriz

# criando lista de palavras
# palavras = []
# print("Você deve digitar até", tamanho_matriz,"palavras com no máximo", tamanho_matriz,"letras")
# for indice_palavra in range(0, tamanho_matriz):
#     sair = 0
#     digite_palavra = 1
#     while(digite_palavra == 1):
#         palavra_digitada = str(input(f'Digite a {indice_palavra+1}a palavra: '))
#         palavra_digitada = palavra_digitada.replace(" ", "")
#         if not palavra_digitada or palavra_digitada.replace(" ", "") == "":
#             sair = 1
#             break
#         else:
#             if(len(palavra_digitada) <= tamanho_matriz):
#                 palavras.append(palavra_digitada)
#                 digite_palavra = 0
#             else:
#                 print("A palavra possui um tamanho não permitido!")
#                 digite_palavra = 1
#     if(sair == 1):
#         break
palavras = ["casa", "luz", "ver", "sol", "buzinha", "madame", "cama", "porta"] # forçando palavras

# lista com as letras do alfabeto
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']

# criando a matriz com letras aleatorias
matriz = []
for numero_linha in range(0, tamanho_colunas_matriz):
    linha = []
    for numero_coluna in range(0, tamanho_linhas_matriz):
        letra_aleatoria = random.choice(letras)
        linha.append(letra_aleatoria)
    matriz.append(linha)
# matriz = [ # forçando valores na matriz
#     ['a', 'b', 'c', 'd'],
#     ['e', 'f', 'g', 'h'],
#     ['i', 'j', 'k', 'l'],
#     ['m', 'n', 'o', 'p']
# ]

# colocando as palavras na matriz
for palavra in palavras:
    tamanho_palavra = len(palavra) # tamanho da palavra
    # direcao = random.choice(["horizontal", "vertical", "diagonal_para_direita", "diagonal_para_esquerda"])
    direcao = "horizontal" # forçando a direcao horizontal
    if(direcao == "horizontal"):
        escolher_posicao = True
        while(escolher_posicao == True):
            print()
            for linha in matriz:
                print(linha)
            # escolhendo posicao aleatoria para a palavra
            linha_palavra = random.randint(0, tamanho_colunas_matriz-1)
            coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
            # checar palavra que já existe na matriz
            palavra_existente = ""
            linha_checagem = linha_palavra
            coluna_checagem = coluna_palavra
            for indice in range(0, tamanho_palavra):
                palavra_existente += matriz[linha_checagem][coluna_checagem]
                coluna_checagem += 1
            print("\nPALAVRA EXISTENTE:", palavra_existente)
            # checar se a palavra não vai sobrepor outra palavra
            palavra_existe = False
            finalizar_checagem = False
            palavras_checagem = palavras
            for palavra_checagem in palavras_checagem:
                if finalizar_checagem == False or palavra_existe == False:
                    palavra_existe = palavra_existente in palavra_checagem
                    print("\n", palavra_checagem, "\n", palavra_existente, "->", palavra_checagem, "=", palavra_existe)
                    if palavra_existe == True:
                        break
                    else:
                        # checando sequência de letras a partir do começo da palavra existente
                        # com isso, a checagem será feita inicialmente para esquerda
                        direcao_checagem = "esquerda"
                        # seleciona a coluna da primeira letra da palavra existente
                        coluna_direcao_checagem = coluna_palavra
                        # começa a busca com a primeira letra da palavra existente
                        palavra_checagem_sequencial = palavra_existente[0]
                        print("PRIMEIRA LETRA CHECAGEM SEQUENCIAL:", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                        # condições para finalizar a checagem
                        while finalizar_checagem == False and palavra_checagem_sequencial in palavra_checagem and len(palavra_checagem_sequencial) <= len(palavra_checagem):
                            # caso a checagem esteja sendo feita para a esquerda
                            if direcao_checagem == "esquerda":
                                print("DIRECAO CHECAGEM:", direcao_checagem)
                                # verifica se possui mais alguma coluna antes da coluna de checagem
                                if coluna_direcao_checagem > 0:
                                    # se possuir, seleciona a coluna anterior
                                    coluna_direcao_checagem -= 1
                                    # adiciona a letra da coluna na palavra checagem sequencial
                                    palavra_checagem_sequencial = matriz[linha_palavra][coluna_direcao_checagem] + palavra_checagem_sequencial
                                    print("PALAVRA CHECAGEM SEQUENCIAL:", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                                # caso não possua mais colunas antes da coluna de checagem,
                                # compara a primeira letra da palavra formada com a primeira letra da palavra da lista
                                elif palavra_checagem_sequencial[0] == palavra_checagem[0]:
                                    # caso sejam iguais, muda o sentido da checagem para a direita
                                    direcao_checagem = "direita"
                                    print("MANDANDO PARA A DIREITA")
                                # caso não tenha mais nenhuma coluna antes da coluna de checagem
                                else:
                                    palavra_existe = False
                                    finalizar_checagem = True
                                    print("FINALIZANDO CHECAGEM")
                            # caso a checagem esteja sendo feita para a direita
                            if direcao_checagem == "direita":
                                coluna_direcao_checagem += len(palavra_checagem_sequencial)
                                print("DIRECAO CHECAGEM:", direcao_checagem)
                                print("PALAVRA CHECAGEM SEQUENCIAL (chegando):", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                                if coluna_direcao_checagem < tamanho_linhas_matriz:
                                    palavra_checagem_sequencial += matriz[linha_palavra][coluna_direcao_checagem]
                                    print("PALAVRA CHECAGEM SEQUENCIAL:", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                                elif palavra_checagem_sequencial == palavra_checagem:
                                    palavra_existe = True
                                    finalizar_checagem = True
                                    print("FINALIZANDO CHECAGEM")
                                else:
                                    palavra_existe = False
                                    finalizar_checagem = True
                                    print("FINALIZANDO CHECAGEM")
                        # testando argumentos do while
                        print("-- TESTANDO ARGUMENTOS DO WHILE --")
                        print("FINALIZAR CHECAGEM:", finalizar_checagem)
                        print("PALAVRA CHECAGEM SEQ. IN PALAVRA CHECAGEM:", palavra_checagem_sequencial in palavra_checagem)
                        print("TAM. PALAVRA CHECAGEM SEQ. <= TAM. PALAVRA CHECAGEM:", len(palavra_checagem_sequencial) <= len(palavra_checagem))
# ATÉ AQUI TÁ DE BOA (de baixo pra cima) ------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        # checando sequência de letras a partir do fim da palavra existente
                        # com isso, a checagem será feita inicialmente para direita
                        direcao_checagem = "direita"
                        # seleciona a coluna da última letra da palavra existente
                        coluna_direcao_checagem = coluna_palavra + len(palavra_existente) - 1
                        # começa a busca com a última letra da palavra existente
                        palavra_checagem_sequencial = palavra_existente[len(palavra_existente)-1]
                        print("PRIMEIRA LETRA CHECAGEM SEQUENCIAL:", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                        # condições para finalizar a checagem
                        while finalizar_checagem == False and palavra_checagem_sequencial in palavra_checagem and len(palavra_checagem_sequencial) <= len(palavra_checagem):
                            # caso a checagem esteja sendo feita para a direita
                            if direcao_checagem == "direita":
                                print("DIRECAO CHECAGEM:", direcao_checagem)
                                # verifica se possui mais alguma coluna após a coluna de checagem
                                if coluna_direcao_checagem < tamanho_linhas_matriz - 1:
                                    # se possuir, seleciona a próxima coluna
                                    coluna_direcao_checagem += 1
                                    # adiciona a letra da próxima coluna na palavra checagem sequencial
                                    palavra_checagem_sequencial += matriz[linha_palavra][coluna_direcao_checagem]
                                    print("PALAVRA CHECAGEM SEQUENCIAL:", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                                # caso não possua mais colunas após a coluna de checagem,
                                # compara a última letra da palavra formada com a última letra da palavra da lista
                                elif palavra_checagem_sequencial[len(palavra_checagem_sequencial)-1] == palavra_checagem[len(palavra_checagem)-1]:
                                    # caso sejam iguais, muda o sentido da checagem para a esquerda
                                    direcao_checagem = "esquerda"
                                    # seleciona a coluna anterior a palavra já formada
                                    coluna_direcao_checagem -= len(palavra_checagem_sequencial)
                                    print("MANDANDO PARA A ESQUERDA")
                                # caso não tenha mais nenhuma coluna após a coluna de checagem
                                # e a última letra da palavra formada não seja igual a última letra da palavra da lista
                                else:
                                    # finaliza a checagem
                                    palavra_existe = False
                                    finalizar_checagem = True
                                    print("FINALIZANDO CHECAGEM")
                            # caso a checagem esteja sendo feita para a esquerda
                            if direcao_checagem == "esquerda":
                                print("DIRECAO CHECAGEM:", direcao_checagem)
                                print("PALAVRA CHECAGEM SEQUENCIAL (chegando):", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                                # caso a coluna de checagem seja a primeira coluna da linha
                                if coluna_direcao_checagem == 0:
                                    # adiciona a letra da coluna na palavra formada
                                    palavra_checagem_sequencial = matriz[linha_palavra][coluna_direcao_checagem] + palavra_checagem_sequencial
                                    print("PALAVRA CHECAGEM SEQUENCIAL:", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                                # caso a coluna de checagem não seja a primeira coluna da linha
                                elif coluna_direcao_checagem > 0:
                                    # adiciona a letra da coluna na palavra formada
                                    palavra_checagem_sequencial = matriz[linha_palavra][coluna_direcao_checagem] + palavra_checagem_sequencial
                                    print("PALAVRA CHECAGEM SEQUENCIAL:", palavra_checagem_sequencial, "\nCOLUNA DIRECAO CHECAGEM:", coluna_direcao_checagem)
                                    # após a adição da letra, seleciona a coluna anterior
                                    coluna_direcao_checagem -= 1
                                    print("COLUNA DIRECAO CHECAGEM SUBTRAIDA:", coluna_direcao_checagem)
                                # caso a palavra formada seja igual a palavra da lista
                                if palavra_checagem_sequencial == palavra_checagem:
                                    # finaliza a checagem informando que a palavra existe
                                    palavra_existe = True
                                    finalizar_checagem = True
                                    print("FINALIZANDO CHECAGEM")
                                # caso a palavra formada não seja igual a palavra da lista
                                else:
                                    # finaliza a checagem informando que a palavra não existe
                                    palavra_existe = False
                                    finalizar_checagem = True
                                    print("FINALIZANDO CHECAGEM")
                        # testando argumentos do while
                        print("-- TESTANDO ARGUMENTOS DO WHILE --")
                        print("FINALIZAR CHECAGEM:", finalizar_checagem)
                        print("PALAVRA CHECAGEM SEQ. IN PALAVRA CHECAGEM:", palavra_checagem_sequencial in palavra_checagem)
                        print("TAM. PALAVRA CHECAGEM SEQ. <= TAM. PALAVRA CHECAGEM:", len(palavra_checagem_sequencial) <= len(palavra_checagem))
            # se a palavra for sobrescrever outra, escolher nova posicao
            if(palavra_existe == True):
                escolher_posicao = True
            # se a palavra não for sobrescrever outra, colocar na matriz
            else:
                escolher_posicao = False
                for letra in palavra:
                    matriz[linha_palavra][coluna_palavra] = letra
                    coluna_palavra += 1
    elif(direcao == "vertical"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-1)
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
    elif(direcao == "diagonal_para_direita"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(0, tamanho_linhas_matriz-tamanho_palavra)
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra += 1
    elif(direcao == "diagonal_para_esquerda"):
        linha_palavra = random.randint(0, tamanho_colunas_matriz-tamanho_palavra)
        coluna_palavra = random.randint(tamanho_palavra-1, tamanho_linhas_matriz-1)
        for letra in palavra:
            matriz[linha_palavra][coluna_palavra] = letra
            linha_palavra += 1
            coluna_palavra -= 1

# printando a matriz
for linha in matriz:
    print(linha)