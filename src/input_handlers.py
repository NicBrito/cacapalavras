from utils import verificar_tentativas_restantes, validar_posicao_usuario, tratar_posicao_usuario
from words import palavras_remover_acentos, palavras_finalizar_coleta, palavras_apenas_letras, palavras_existe, palavras_tamanho, palavras_registrar

# definindo tamanho da matriz
def matriz_solicitar_tamanho():
    tentativas = 3 # definindo a quantidade de tentativas para digitar o tamanho da matriz
    while(verificar_tentativas_restantes(tentativas)): # caso precise digitar novo valor para o tamanho da matriz
        tamanho_matriz = input("Defina o tamanho da matriz quadrada: ") # definindo o tamanho da matriz
        if(tamanho_matriz.isdigit() and int(tamanho_matriz) > 1): # caso o tamanho da matriz seja um número inteiro e maior que um
            tamanho_matriz = int(tamanho_matriz) # convertendo o tamanho da matriz para um número inteiro
            tamanho_linhas_matriz = tamanho_matriz # definindo o tamanho das linhas da matriz
            tamanho_colunas_matriz = tamanho_matriz # definindo o tamanho das colunas da matriz
            break # finalizando a definição do tamanho da matriz
        else: # caso o tamanho da matriz não seja um número inteiro e maior que um
            print("O tamanho da matriz deve ser um número inteiro e maior que um!") # informando que o tamanho da matriz deve ser um número inteiro e maior que um
            tentativas -= 1 # decrementando a quantidade de tentativas
    return tamanho_matriz, tamanho_linhas_matriz, tamanho_colunas_matriz # retornando valores da matriz

# criando lista de palavras
def palavras_coletar(tamanho_matriz):
    print("Você deve digitar até", tamanho_matriz, "palavras que tenham mais de uma letra e no máximo", tamanho_matriz, "letras!"
          "\nPara finalizar a digitação, digite ENTER") # informando a quantidade de palavras que o usuário deve digitar
    palavras = {} # criando dicionário de palavras
    tentativas = 3 # definindo a quantidade de tentativas para digitar as palavras
    for indice in range(0, tamanho_matriz): # percorrendo a quantidade de palavras que o usuário deve digitar
        while(verificar_tentativas_restantes(tentativas)): # caso deva digitar uma nova palavra
            palavra_digitada = palavras_remover_acentos(str(input(f'Digite a {indice+1}a palavra: ')).upper().replace(" ", "")) # pegando a palavra digitada, convertendo para maiúsculo e removendo espaços e acentos
            if(palavras_finalizar_coleta(palavra_digitada)): # caso o usuário não digite nada ou apenas espaços
                break # finalizando a digitação de palavras
            if(palavras_apenas_letras(palavra_digitada) # caso a palavra possua apenas letras
               and not palavras_existe(palavras, palavra_digitada) # caso a palavra não exista
               and palavras_tamanho(palavra_digitada, tamanho_matriz)): # caso a palavra possua um tamanho permitido
                palavras = palavras_registrar(palavras, palavra_digitada) # registrando a palavra
                break # finalizando a digitação de palavras
            else: # caso a palavra não possua um tamanho permitido, já exista ou não possua apenas letras
                tentativas -= 1 # decrementando a quantidade de tentativas
        if(palavras_finalizar_coleta(palavra_digitada)): # caso deva finalizar a digitação de palavras antes do máximo possível
            break # finalizando a digitação de palavras
    return palavras # retornando lista de palavras

# função para solicitar a posição da palavra ao usuário
def buscador_solicitar_posicao(tamanho_matriz):
    tentativas = 3 # quantidade de tentativas para o usuário digitar uma posição válida
    print(f'\nPara finalizar a digitação, digite ENTER') # informando ao usuário como finalizar a procura de palavras
    for indice in range(0, 2): # pedindo as posições da palavra ao usuário
        while(verificar_tentativas_restantes(tentativas)): # enquanto a posição for inválida
            posicao = input(f'Digite a posição {["inicial", "final"][indice]} da palavra (linha, coluna): ') # pedindo a posição da palavra
            if(palavras_finalizar_coleta(posicao)): # verificando se o usuário deseja encerrar a procura de palavras
                return '', '' # encerrando a procura de palavras
            if(validar_posicao_usuario(posicao, tamanho_matriz)): # verificando se a posição dita pelo usuário é válida
                if(indice == 1 and tratar_posicao_usuario(posicao) == posicao_inicial): # verificando se a posição final é igual a posição inicial
                    print('Posição final não pode ser igual a posição inicial! Digite uma posição válida.') # informando ao usuário que a posição final não pode ser igual a posição inicial
                else: # caso a posição final não seja igual a posição inicial
                    break # não pedir nova posição
            tentativas -= 1 # decrementando a quantidade de tentativas, caso a posição seja inválida
        if(indice == 0): # verificando se é a posição inicial
            posicao_inicial = tratar_posicao_usuario(posicao) # criando a tupla da posição inicial
        else: # caso seja a posição final
            posicao_final = tratar_posicao_usuario(posicao) # criando a tupla da posição final
    return posicao_inicial, posicao_final # retornando a posição inicial e final