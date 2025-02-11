import os
import json
from ..word_search.utils import verificar_tentativas_restantes

DATA_PATH = "data/users/" # caminho da pasta de usuários
FILE_PATH = os.path.join(DATA_PATH, "users.json") # caminho do arquivo de usuários

# função para verificar se o usuário já existe
def usuario_existe(usuario_nome):
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
            for usuario in usuarios: # para cada usuário no arquivo
                if(usuario["usuario_nome"] == usuario_nome): # se o nome do usuário no arquivo for igual ao nome do usuário digitado
                    return True # retornar que o nome do usuário já existe
    except FileNotFoundError: # se o arquivo de usuários não existir
        return False # retornar que o nome do usuário não existe
    return False # retornar que o nome do usuário não existe

# função para salvar o usuário no arquivo
def usuario_salvar(usuario_conta):
    os.makedirs(DATA_PATH, exist_ok = True) # criando o diretório de usuários, caso não exista
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
    except FileNotFoundError: # se o arquivo de usuários não existir
        usuarios = [] # definindo a lista de usuários como vazia
    usuarios.append(usuario_conta) # adicionando a conta do usuário na lista de usuários
    with open(FILE_PATH, "w") as arquivo: # abrindo o arquivo de usuários
        json.dump(usuarios, arquivo, indent = 4) # salvando a lista de usuários no arquivo

# função para remover o usuário do arquivo
def usuario_remover(usuario_conta):
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
    except FileNotFoundError: # se o arquivo de usuários não existir
        return # caso o arquivo de usuários não exista, não é necessário remover o usuário
    usuarios.remove(usuario_conta) # removendo a conta do usuário da lista de usuários
    with open(FILE_PATH, "w") as arquivo: # abrindo o arquivo de usuários
        json.dump(usuarios, arquivo, indent = 4) # salvando a lista de usuários no arquivo

# função para verificar se o usuário possui dados
def usuario_possui_dados(usuario_conta):
    USER_DATA_PATH = os.path.join("data/user/", usuario_conta["usuario_nome"]) # caminho da pasta de dados do usuário
    return os.path.exists(USER_DATA_PATH) # retornando se a pasta de dados do usuário existe

# função para verificar se existe usuários no arquivo
def usuarios_existe():
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
            if(usuarios): # se houver usuários no arquivo
                return True # retornar que existem usuários no arquivo
    except FileNotFoundError: # se o arquivo de usuários não existir
        return False # retornar que não existem usuários no arquivo
    return False # retornar que não existem usuários no arquivo

# função para remover todos os usuários do arquivo
def usuarios_remover():
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
    except FileNotFoundError: # se o arquivo de usuários não existir
        return # caso o arquivo de usuários não exista, não é necessário remover os usuários
    usuarios.clear() # removendo todos os usuários da lista de usuários
    with open(FILE_PATH, "w") as arquivo: # abrindo o arquivo de usuários
        json.dump(usuarios, arquivo, indent = 4) # salvando a lista de usuários no arquivo

# função para apagar arquivo de usuários
def usuarios_apagar_arquivo():
    usuarios_remover() # apagando todos os usuários do arquivo
    os.remove(FILE_PATH) # apagando o arquivo de usuários

# função para verificar se a conta do usuário existe
def conta_existe(usuario_conta):
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
            for usuario in usuarios: # para cada usuário no arquivo
                if(usuario["usuario_nome"] == usuario_conta["usuario_nome"] and
                   usuario["usuario_senha"] == usuario_conta["usuario_senha"]): # se a conta do usuário no arquivo for igual a conta do usuário digitada
                    return True # retornar que a conta do usuário existe
    except FileNotFoundError: # se o arquivo de usuários não existir
        return False # retornar que a conta do usuário não existe
    return False # retornar que a conta do usuário não existe

# função para obter os dados da conta do usuário
def conta_dados(usuario_conta):
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
            for usuario in usuarios: # para cada usuário no arquivo
                if(usuario["usuario_nome"] == usuario_conta["usuario_nome"] and
                   usuario["usuario_senha"] == usuario_conta["usuario_senha"]): # se a conta do usuário no arquivo for igual a conta do usuário digitada
                    return usuario # retornar os dados da conta do usuário
    except FileNotFoundError: # se o arquivo de usuários não existir
        return {} # retornar um dicionário vazio
    return {} # retornar um dicionário vazio

# função para apagar os dados da conta do usuário
def conta_apagar_dados(usuario_conta):
    USER_DATA_PATH = os.path.join("data/user/", usuario_conta["usuario_nome"]) # caminho da pasta de dados do usuário
    for arquivo in os.listdir(USER_DATA_PATH): # para cada arquivo na pasta de dados do usuário
        os.remove(os.path.join(USER_DATA_PATH, arquivo)) # apagando o arquivo
    os.rmdir(USER_DATA_PATH) # apagando a pasta de dados do usuário

# função para apagar a conta do usuário
def conta_apagar(usuario_conta):
    tentativas = 3 # definindo a quantidade de tentativas do usuário
    if(usuario_conta["cacapalavras_salvos"] != 0 or usuario_conta["listas_palavras"] != 0): # caso o usuário tenha criado um caça-palavras ou uma lista de palavras
        os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
        print("Você deseja apagar todos os dados salvos?\n\n"
                "1- SIM\n"
                "2- NÃO\n") # perguntando ao usuário se ele deseja apagar todos os dados salvos
        while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário tiver tentativas, ele poderá escolher uma opção
            opcao_apagar_todos_dados = input("Digite a opção que deseja acessar: ") # solicitando ao usuário que escolha uma opção
            if(opcao_apagar_todos_dados != '1' and opcao_apagar_todos_dados != '2'): # caso o usuário escolha uma opção inválida
                print("Opção inválida! Digite uma opção válida.\n") # informando ao usuário que a opção escolhida é inválida
                tentativas -= 1 # decrementando a quantidade de tentativas
                continue # solicitando ao usuário que escolha uma nova opção
            usuario_remover(usuario_conta) # apagando a conta do usuário
            if not (usuarios_existe()): # caso não haja usuários no arquivo
                usuarios_apagar_arquivo() # apagando o arquivo de usuários
            if(opcao_apagar_todos_dados == '1'): # caso o usuário escolha a opção "Sim"
                conta_apagar_dados(usuario_conta) # apagando os dados da conta do usuário
                return "Conta e dados apagados" # retornando ao menu principal
            return "Conta apagada, dados mantidos" # retornando ao menu principal
    usuario_remover(usuario_conta) # apagando a conta do usuário
    try: # caso o arquivo de dados do usuário ainda exista
        conta_apagar_dados(usuario_conta) # apagando os dados da conta do usuário
    except FileNotFoundError: # caso o arquivo de dados do usuário não exista
        pass # não é necessário apagar os dados da conta do usuário
    if not (usuarios_existe()): # caso não haja usuários no arquivo
        usuarios_apagar_arquivo() # apagando o arquivo de usuários
    return "Conta apagada" # retornando ao menu principal

# função para atualizar a conta do usuário
def conta_atualizar(usuario_conta, atualizacao):
    usuario_remover(usuario_conta) # apagando a conta do usuário
    match atualizacao: # verificando a atualização a ser feita
        case "adicionar cacapalavras_salvos": # caso a atualização seja "adicionar cacapalavras_salvos"
            usuario_conta["cacapalavras_salvos"] += 1 # incrementando a quantidade de caça-palavras salvos
        case "remover cacapalavras_salvos": # caso a atualização seja "remover cacapalavras_salvos"
            usuario_conta["cacapalavras_salvos"] -= 1 # decrementando a quantidade de caça-palavras salvos
        case "adicionar listas_palavras": # caso a atualização seja "adicionar listas_palavras"
            usuario_conta["listas_palavras"] += 1 # incrementando a quantidade de listas de palavras
        case "remover listas_palavras": # caso a atualização seja "remover listas_palavras"
            usuario_conta["listas_palavras"] -= 1 # decrementando a quantidade de listas de palavras
    usuario_salvar(usuario_conta) # salvando a conta do usuário

# função para carregar dados na conta do usuário
def conta_carregar_dados(usuario_conta, dados):
    usuario_remover(usuario_conta) # apagando a conta do usuário
    usuario_conta["cacapalavras_salvos"] = dados["cacapalavras_salvos"] # carregando a quantidade de caça-palavras salvos
    usuario_conta["listas_palavras"] = dados["listas_palavras"] # carregando a quantidade de listas de palavras salvas
    usuario_salvar(usuario_conta) # salvando a conta do usuário