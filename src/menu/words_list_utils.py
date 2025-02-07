import os
import json
from ..word_search.utils import verificar_tentativas_restantes
from ..word_search.words import palavras_remover_acentos, palavras_finalizar_coleta, palavras_apenas_letras, palavras_existe

# função para obter o caminho do arquivo
def obter_caminho_arquivo(usuario_conta):
    usuario_nome = usuario_conta["usuario_nome"] # obtendo o nome do usuário
    data_path = os.path.join("data", "user", usuario_nome) # definindo o caminho do arquivo
    os.makedirs(data_path, exist_ok=True) # criando o diretório, se não existir
    return os.path.join(data_path, "words_list.json") # retornando o caminho do arquivo

# função para carregar as listas de palavras do arquivo
def carregar_listas_palavras(file_path):
    if not os.path.exists(file_path): # caso o arquivo não exista
        return [] # retornar uma lista vazia
    with open(file_path, "r") as arquivo: # abrindo o arquivo
        return json.load(arquivo) # retornando o conteúdo do arquivo

# função para salvar as listas de palavras no arquivo
def salvar_listas_palavras(file_path, listas_palavras):
    with open(file_path, "w") as arquivo: # abrindo o arquivo
        json.dump(listas_palavras, arquivo, indent=4) # salvando as listas de palavras no arquivo

# função para salvar uma nova lista de palavras
def salvar_lista_palavras(usuario_conta, lista_palavras):
    file_path = obter_caminho_arquivo(usuario_conta) # obtendo o caminho do arquivo
    listas_palavras = carregar_listas_palavras(file_path) # carregando as listas de palavras do arquivo
    listas_palavras.append(lista_palavras) # adicionando a nova lista de palavras
    salvar_listas_palavras(file_path, listas_palavras) # salvando as listas de palavras no arquivo

# função para contar as listas de palavras
def contar_listas_palavras(usuario_conta):
    file_path = obter_caminho_arquivo(usuario_conta) # obtendo o caminho do arquivo
    listas_palavras = carregar_listas_palavras(file_path) # carregando as listas de palavras do arquivo
    return len(listas_palavras) # retornando a quantidade de listas de palavras

# função para exibir as listas de palavras salvas
def exibir_listas_palavras(usuario_conta):
    file_path = obter_caminho_arquivo(usuario_conta) # obtendo o caminho do arquivo
    listas_palavras = carregar_listas_palavras(file_path) # carregando as listas de palavras do arquivo
    if not listas_palavras: # caso não haja listas de palavras salvas
        print("Nenhuma lista de palavras salva!\n") # informar ao usuário que não há listas de palavras salvas
        return # finalizando a função
    print("LISTAS DE PALAVRAS SALVAS:\n") # informar ao usuário que as listas de palavras serão exibidas
    for indice, lista_palavras in enumerate(listas_palavras, start=1): # percorrendo as listas de palavras
        print(f"{indice}. {lista_palavras['lista_nome']}\n{", ".join(lista_palavras['palavras'])}\n") # exibindo as listas de palavras

# função para exibir uma lista de palavras
def exibir_lista_palavras(lista_palavras):
    print(f"LISTA:\n\n{lista_palavras['lista_nome']}") # informando ao usuário o nome da lista de palavras exibida
    for indice, palavra in enumerate(lista_palavras["palavras"], start=1): # percorrendo as palavras da lista de palavras
        print(f"{indice}. {palavra}") # exibindo as palavras da lista de palavras
    print() # pulando uma linha

# função para verificar se uma lista de palavras já existe
def lista_palavras_existe(usuario_conta, lista_palavras):
    file_path = obter_caminho_arquivo(usuario_conta) # obtendo o caminho do arquivo
    listas_palavras = carregar_listas_palavras(file_path) # carregando as listas de palavras do arquivo
    for lista in listas_palavras: # percorrendo as listas de palavras
        if(lista["lista_nome"] == lista_palavras): # verificando se a lista de palavras já existe
            return True # retornando que a lista de palavras já existe
    return False # retornando que a lista de palavras não existe

# função para criar uma nova lista de palavras
def criar_lista_palavras(usuario_conta):
    print("NOVA LISTA DE PALAVRAS\n"
          "\nPara cancelar, digite ENTER\n") # informando ao usuário que a criação de uma nova lista de palavras foi iniciada e como cancelar
    tentativas = 3 # definindo a quantidade de tentativas para digitar o nome da lista de palavras
    while(verificar_tentativas_restantes(tentativas)): # caso deva digitar o nome da lista de palavras
        lista_nome = palavras_remover_acentos(str(input('Digite o nome da lista de palavras: ')).upper()) # pegando o nome da lista de palavras, convertendo para maiúsculo e removendo acentos
        if(palavras_finalizar_coleta(lista_nome)): # caso o usuário não digite nada ou apenas espaços
            return # cancelando a criação da lista de palavras
        if(lista_palavras_existe(usuario_conta, lista_nome)): # caso a lista de palavras já exista
            print("Lista de palavras já existe!\n") # informando ao usuário que a lista de palavras já existe
            tentativas -= 1 # decrementando a quantidade de tentativas
        else: # caso a lista de palavras não exista
            break # finalizando a digitação do nome da lista de palavras
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    print("NOVA LISTA DE PALAVRAS\n"
         f'\nDigite as palavras da lista "{lista_nome}"'
          "\nPara finalizar, digite ENTER\n") # informando ao usuário que a criação das palavras da lista de palavras foi iniciada e como finalizar
    palavras = [] # criando lista de palavras
    indice = 0 # definindo o índice inicial
    tentativas = 3 # definindo a quantidade de tentativas para digitar as palavras
    while(verificar_tentativas_restantes(tentativas)): # caso deva digitar uma nova palavra
        indice += 1 # incrementando o índice
        palavra_digitada = palavras_remover_acentos(str(input(f'Digite a {indice}a palavra: ')).upper().replace(" ", "")) # pegando a palavra digitada, convertendo para maiúsculo e removendo espaços e acentos
        if(palavras_finalizar_coleta(palavra_digitada)): # caso o usuário digite nada ou apenas espaços
            break # finalizando a digitação de palavras
        if(palavras_apenas_letras(palavra_digitada) and # caso a palavra possua apenas letras
           not palavras_existe(palavras, palavra_digitada)): # caso a palavra não exista
            palavras.append(palavra_digitada) # adicionando a palavra à lista de palavras
        else: # caso a palavra já exista ou não possua apenas letras
            tentativas -= 1 # decrementando a quantidade de tentativas
    if not (palavras): # caso não haja palavras na lista
        return # cancelando a criação da lista de palavras
    lista_tamanho = len(palavras) # definindo o tamanho da lista de palavras
    tamanho_maior_palavra = max([len(palavra) for palavra in palavras]) # definindo o tamanho da maior palavra
    lista_palavras = {"lista_nome": lista_nome,
                      "palavras": palavras,
                      "lista_tamanho": lista_tamanho,
                      "tamanho_maior_palavra": tamanho_maior_palavra} # criando a lista de palavras
    return lista_palavras # retornando a lista de palavras

# função para remover uma lista de palavras
def remover_lista_palavras(usuario_conta):
    file_path = obter_caminho_arquivo(usuario_conta) # obtendo o caminho do arquivo
    listas_palavras = carregar_listas_palavras(file_path) # carregando as listas de palavras do arquivo
    lista_nome = palavras_remover_acentos(str(input('Digite o nome da lista de palavras: ')).upper()) # pegando o nome da lista de palavras, convertendo para maiúsculo e removendo acentos
    if(palavras_finalizar_coleta(lista_nome)): # caso o usuário não digite nada ou apenas espaços
        return 'Cancelar remoção' # cancelando a remoção da lista de palavras
    if(lista_palavras_existe(usuario_conta, lista_nome)): # verificando se a lista de palavras existe
        listas_palavras = [lista for lista in listas_palavras if lista["lista_nome"] != lista_nome] # removendo a lista de palavras
        salvar_listas_palavras(file_path, listas_palavras) # salvando as listas de palavras no arquivo
        return 'Lista removida' # retornando que a lista de palavras foi removida
    return 'Lista não encontrada' # retornando que a lista de palavras não foi encontrada

# função para atualizar a lista de palavras
def atualizar_lista_palavras(usuario_conta, lista_palavras, atualizacao):
    file_path = obter_caminho_arquivo(usuario_conta) # obtendo o caminho do arquivo
    listas_palavras = carregar_listas_palavras(file_path) # carregando as listas de palavras do arquivo
    match atualizacao: # verificando qual atualização deve ser feita
        case "adicionar lista_palavras": # caso a atualização seja "adicionar lista_palavras"
            listas_palavras.append(lista_palavras) # adicionando a lista de palavras
        case "remover lista_palavras": # caso a atualização seja "remover lista_palavras"
            listas_palavras = [lista for lista in listas_palavras if lista["lista_nome"] != lista_palavras["lista_nome"]] # removendo a lista de palavras
    salvar_listas_palavras(file_path, listas_palavras) # salvando as listas de palavras no arquivo

# função para encontrar uma palavra em uma lista de palavras
def encontrar_palavra_lista_palavras(lista_palavras, palavra):
    for palavra_lista in lista_palavras["palavras"]: # para cada palavra na lista de palavras
        if(palavra == palavra_lista): # caso a palavra seja igual à palavra da lista de palavras
            return True # retornar que a palavra foi encontrada
    return False # retornar que a palavra não foi encontrada

# função para trocar uma palavra de uma lista de palavras
def trocar_palavra_lista_palavras(usuario_conta, lista_palavras, palavra):
    tentativas = 3 # definindo a quantidade de tentativas para digitar a nova palavra
    while(verificar_tentativas_restantes(tentativas)): # caso deva digitar a nova palavra
        palavra_nova = palavras_remover_acentos(str(input('Digite a nova palavra: ')).upper().replace(" ", "")) # pegando a nova palavra digitada, convertendo para maiúsculo e removendo espaços e acentos
        if(palavras_finalizar_coleta(palavra_nova)): # caso o usuário digite nada ou apenas espaços
            return 'Cancelar edição' # cancelando a edição da palavra
        if(encontrar_palavra_lista_palavras(lista_palavras, palavra_nova)): # caso a nova palavra já exista
            print("Palavra já existe na lista de palavras!\n") # informando ao usuário que a nova palavra já existe
            tentativas -= 1 # decrementando a quantidade de tentativas
        else: # caso a nova palavra não exista
            atualizar_lista_palavras(usuario_conta, lista_palavras, "remover lista_palavras") # removendo a lista de palavras
            lista_palavras["palavras"] = [palavra_nova if palavra == palavra_lista else palavra_lista for palavra_lista in lista_palavras["palavras"]] # trocando a palavra da lista de palavras
            atualizar_lista_palavras(usuario_conta, lista_palavras, "adicionar lista_palavras") # atualizando a lista de palavras
            return 'Palavra editada' # retornando que a palavra foi editada

# função para editar palavras de uma lista de palavras
def editar_lista_palavras_palavras(usuario_conta, lista_palavras):
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
    print("EDITAR LISTA DE PALAVRAS\n"
          "\nPara cancelar, digite ENTER\n") # informando ao usuário que a edição das palavras da lista de palavras foi iniciada e como cancelar
    tentativas = 3 # definindo a quantidade de tentativas para digitar as palavras
    while(verificar_tentativas_restantes(tentativas)): # caso deva digitar uma nova palavra
        palavra_digitada = palavras_remover_acentos(str(input('Digite a palavra que deseja editar: ')).upper().replace(" ", "")) # pegando a palavra digitada, convertendo para maiúsculo e removendo espaços e acentos
        if(palavras_finalizar_coleta(palavra_digitada)): # caso o usuário digite nada ou apenas espaços
            return 'Cancelar edição' # cancelando a edição das palavras da lista de palavras
        if not (encontrar_palavra_lista_palavras(lista_palavras, palavra_digitada)): # caso a palavra não exista
            print("Palavra não encontrada!\n") # informando ao usuário que a palavra não foi encontrada
            tentativas -= 1 # decrementando a quantidade de tentativas
        else: # caso a palavra exista
            retorno_trocar_palavras = trocar_palavra_lista_palavras(usuario_conta, lista_palavras, palavra_digitada) # trocando a palavra da lista de palavras
            if(retorno_trocar_palavras == 'Palavra editada'): # caso a palavra seja editada
                return 'Palavra editada' # retornando que a palavra foi editada
            elif(retorno_trocar_palavras == 'Cancelar edição'): # caso a edição da palavra seja cancelada
                return 'Cancelar edição' # cancelando a edição da palavra

# função para editar nome de uma lista de palavras
def editar_lista_palavras_nome(usuario_conta, lista_palavras):
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
    print("EDITAR LISTA DE PALAVRAS\n"
          "\nPara cancelar, digite ENTER\n") # informando ao usuário que a edição do nome da lista de palavras foi iniciada e como cancelar
    tentativas = 3 # definindo a quantidade de tentativas para digitar o novo nome da lista de palavras
    while(verificar_tentativas_restantes(tentativas)): # enquanto houver tentativas para editar o nome da lista de palavras
        novo_nome = palavras_remover_acentos(str(input('Digite o novo nome da lista de palavras: ')).upper()) # pegando o novo nome da lista de palavras, convertendo para maiúsculo e removendo acentos
        if(palavras_finalizar_coleta(novo_nome)): # caso o usuário não digite nada ou apenas espaços
            return 'Cancelar edição' # cancelando a edição do nome da lista de palavras
        if(lista_palavras_existe(usuario_conta, novo_nome)): # caso o novo nome da lista de palavras já exista
            print("Nome já está em uso!\n") # informando ao usuário que o novo nome da lista de palavras já existe
            tentativas -= 1 # decrementando a quantidade de tentativas
        else: # caso o novo nome da lista de palavras não exista
            break # finalizando a digitação do novo nome da lista de palavras
    atualizar_lista_palavras(usuario_conta, lista_palavras, "remover lista_palavras") # removendo a lista de palavras
    lista_palavras["lista_nome"] = novo_nome # atualizando o nome da lista de palavras
    atualizar_lista_palavras(usuario_conta, lista_palavras, "adicionar lista_palavras") # adicionando a lista de palavras
    return 'Nome editado' # retornando que o nome da lista de palavras foi editado

# função para exibir as opções de edição de uma lista de palavras
def exibir_opcoes_edicao_lista_palavras():
    print("EDITAR LISTA DE PALAVRAS\n\n"
          "1- EDITAR NOME DA LISTA DE PALAVRAS\n"
          "2- EDITAR PALAVRAS DA LISTA DE PALAVRAS\n"
          "3- VOLTAR\n") # exibindo as opções de edição da lista de palavras

# função para exibir e editar a lista de palavras selecionada
def editar_lista_palavras_selecionada(usuario_conta, lista_nome):
    file_path = obter_caminho_arquivo(usuario_conta) # obtendo o caminho do arquivo
    listas_palavras = carregar_listas_palavras(file_path) # carregando as listas de palavras do arquivo
    lista_palavras = [lista for lista in listas_palavras if lista["lista_nome"] == lista_nome][0] # obtendo a lista de palavras selecionada
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
    tentativas = 3 # definindo a quantidade de tentativas para escolher uma opção
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário não sair do menu
        exibir_opcoes_edicao_lista_palavras() # exibindo as opções de edição da lista de palavras
        opcao_escolhida = input("Digite a opção que deseja acessar: ") # solicitando ao usuário que escolha uma opção
        if(opcao_escolhida == '1'): # caso o usuário escolha a opção "Editar nome da lista de palavras"
            retorno_editar_nome = editar_lista_palavras_nome(usuario_conta, lista_palavras) # editando o nome da lista de palavras
            if(retorno_editar_nome == 'Nome editado'): # caso o nome da lista de palavras seja editado
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
                print("Nome da lista de palavras editado com sucesso!\n") # informando ao usuário que o nome da lista de palavras foi editado
            elif(retorno_editar_nome == 'Cancelar edição'): # caso a edição do nome da lista de palavras seja cancelada
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
                continue # solicitando ao usuário que escolha uma nova opção de edição da lista de palavras
        elif(opcao_escolhida == '2'): # caso o usuário escolha a opção "Editar palavras da lista de palavras"
            retorno_editar_palavras = editar_lista_palavras_palavras(usuario_conta, lista_palavras) # editando as palavras da lista de palavras
            if(retorno_editar_palavras == 'Palavra editada'): # caso a palavra seja editada
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
                print("Palavra editada com sucesso!\n") # informando ao usuário que a palavra foi editada
            elif(retorno_editar_palavras == 'Cancelar edição'): # caso a edição da palavra seja cancelada
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
                continue # solicitando ao usuário que escolha uma nova opção de edição da lista de palavras
        elif(opcao_escolhida == '3'): # caso o usuário escolha a opção "Voltar"
            return 'Voltar' # voltando ao menu de escolha de listas de palavras
        else: # caso o usuário escolha uma opção inválida
            tentativas -= 1 # decrementando a quantidade de tentativas
            if(tentativas == 0): # caso o usuário não tenha mais tentativas
                continue # encerrando o menu de edição da lista de palavras
            os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
            exibir_lista_palavras(lista_palavras) # exibindo a lista de palavras selecionada
            print("Opção inválida! Digite uma opção válida.\n") # informando ao usuário que a opção escolhida é inválida

# função para editar uma lista de palavras
def editar_lista_palavras(usuario_conta):
    lista_nome = palavras_remover_acentos(str(input('Digite o nome da lista de palavras: ')).upper()) # pegando o nome da lista de palavras, convertendo para maiúsculo e removendo acentos
    if(palavras_finalizar_coleta(lista_nome)): # caso o usuário não digite nada ou apenas espaços
        return 'Cancelar edição' # cancelando a edição da lista de palavras
    if(lista_palavras_existe(usuario_conta, lista_nome)): # verificando se a lista de palavras existe
        retorno_editar_lista_palavras = editar_lista_palavras_selecionada(usuario_conta, lista_nome) # editando a lista de palavras selecionada
        if(retorno_editar_lista_palavras == 'Cancelar edição'): # caso a edição da lista de palavras seja cancelada
            return 'Cancelar edição' # cancelando a edição da lista de palavras
        elif(retorno_editar_lista_palavras == 'Voltar'): # caso o usuário escolha a opção "Voltar"
            return # solicitanco ao usuário que escolha uma nova lista para editar
        return 'Lista editada' # retornando que a lista de palavras foi editada
    return 'Lista não encontrada' # retornando que a lista de palavras não foi encontrada