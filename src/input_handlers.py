from utils import verificar_tentativas_restantes, validar_posicao_de_entrada, transformar_string_em_tupla, validar_posicoes_da_palavra
from words import palavras_remover_acentos, palavras_finalizar_coleta, palavras_apenas_letras, palavras_existe, palavras_tamanho, palavras_registrar

# definindo tamanho da matriz
def matriz_solicitar_tamanho():
    tentativas = 3 # definindo a quantidade de tentativas para digitar o tamanho da matriz
    for indice in range(0, 2): # definindo a quantidade de interações para definir o tamanho da matriz (linhas:0, colunas:1)
        while(verificar_tentativas_restantes(tentativas)): # caso precise digitar nova quantidade de linhas ou colunas
            quantidade = input(f'Digite a quantidade de {["linhas", "colunas"][indice]} da matriz: ') # solicitando a quantidade de linhas ou colunas da matriz
            if(quantidade.isdigit() and int(quantidade) > 1): # caso a quantidade seja um número inteiro e maior que um
                break # finalizando a solicitação da quantidade
            print(f'A quantidade de {["linhas", "colunas"][indice]} deve ser um número inteiro e maior que um!') # informando que a quantidade de linhas e colunas deve ser um número inteiro e maior que um
            tentativas -= 1 # decrementando a quantidade de tentativas
        match indice: # verificando se é a quantidade de linhas ou colunas
            case 0: quantidade_linhas = int(quantidade) # definindo a quantidade de linhas
            case 1: quantidade_colunas = int(quantidade) # definindo a quantidade de colunas
    tamanho_menor_matriz = min(quantidade_linhas, quantidade_colunas) # definindo o menor tamanho da matriz
    return tamanho_menor_matriz, quantidade_colunas, quantidade_linhas # retornando valores da matriz

# criando lista de palavras
def palavras_coletar(tamanho_menor_matriz):
    print("Você deve digitar até", tamanho_menor_matriz, "palavras que tenham mais de uma letra e no máximo", tamanho_menor_matriz, "letras!"
          "\nPara finalizar a digitação, digite ENTER") # informando a quantidade de palavras que o usuário deve digitar
    palavras = {} # criando dicionário de palavras
    tentativas = 3 # definindo a quantidade de tentativas para digitar as palavras
    for indice in range(0, tamanho_menor_matriz): # percorrendo a quantidade de palavras que o usuário deve digitar
        while(verificar_tentativas_restantes(tentativas)): # caso deva digitar uma nova palavra
            palavra_digitada = palavras_remover_acentos(str(input(f'Digite a {indice+1}a palavra: ')).upper().replace(" ", "")) # pegando a palavra digitada, convertendo para maiúsculo e removendo espaços e acentos
            if(palavras_finalizar_coleta(palavra_digitada)): # caso o usuário não digite nada ou apenas espaços
                break # finalizando a digitação de palavras
            if(palavras_apenas_letras(palavra_digitada) # caso a palavra possua apenas letras
               and not palavras_existe(palavras, palavra_digitada) # caso a palavra não exista
               and palavras_tamanho(palavra_digitada, tamanho_menor_matriz)): # caso a palavra possua um tamanho permitido
                palavras = palavras_registrar(palavras, palavra_digitada) # registrando a palavra
                break # finalizando a digitação de palavras
            else: # caso a palavra não possua um tamanho permitido, já exista ou não possua apenas letras
                tentativas -= 1 # decrementando a quantidade de tentativas
        if(palavras_finalizar_coleta(palavra_digitada)): # caso deva finalizar a digitação de palavras antes do máximo possível
            break # finalizando a digitação de palavras
    return palavras # retornando lista de palavras

# função para solicitar a posição da palavra ao usuário
def buscador_solicitar_posicao(matriz):
    tentativas = 3 # quantidade de tentativas para o usuário digitar uma posição válida
    print(f'\nPara finalizar a digitação, digite ENTER') # informando ao usuário como finalizar a procura de palavras
    for indice, tipo_posicao in enumerate(["inicial", "final"]): # iterando para definir a posição inicial e final
        while(verificar_tentativas_restantes(tentativas)): # enquanto a posição for inválida
            posicao = input(f'Digite a posição {tipo_posicao} da palavra (linha, coluna): ') # pedindo a posição da palavra
            if(palavras_finalizar_coleta(posicao)): # verificando se o usuário deseja encerrar a procura de palavras
                return '', '' # encerrando a procura de palavras
            if not (validar_posicao_de_entrada(matriz, posicao)): # verificando se a posição dita pelo usuário é inválida
                tentativas -= 1 # decrementando a quantidade de tentativas
                continue # pedindo nova posição
            posicao_tupla = transformar_string_em_tupla(posicao) # transformando a posição em tupla
            if(indice == 1): # verificando se é a posição final
                if(posicao_tupla == posicao_inicial): # verificando se a posição final é igual a posição inicial
                    print('Posição final não pode ser igual a posição inicial! Digite uma posição válida.') # informando ao usuário que a posição final não pode ser igual a posição inicial
                    tentativas -= 1 # decrementando a quantidade de tentativas
                    continue # pedindo nova posição
                if not (validar_posicoes_da_palavra(posicao_inicial, posicao_tupla)): # verificando se as posições estão alinhadas
                    print('As posições devem estar alinhadas (horizontal, vertical ou diagonal)! Digite uma posição válida.') # informando ao usuário que as posições devem estar alinhadas
                    tentativas -= 1 # decrementando a quantidade de tentativas
                    continue # pedindo nova posição
            break # finalizando a solicitação da posição
        if(indice == 0): # verificando se é a posição inicial
            posicao_inicial = posicao_tupla # definindo a posição inicial
        else: # caso seja a posição final
            posicao_final = posicao_tupla # definindo a posição final
    return posicao_inicial, posicao_final # retornando a posição inicial e final