import os, json

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

# função para verificar se a conta do usuário existe
def conta_existe(usuario_conta):
    try: # tentando abrir o arquivo de usuários
        with open(FILE_PATH, "r") as arquivo: # abrindo o arquivo de usuários
            usuarios = json.load(arquivo) # carregando os usuários do arquivo
            for usuario in usuarios: # para cada usuário no arquivo
                if(usuario == usuario_conta): # se a conta do usuário no arquivo for igual a conta do usuário digitada
                    return True # retornar que a conta do usuário existe
    except FileNotFoundError: # se o arquivo de usuários não existir
        return False # retornar que a conta do usuário não existe
    return False # retornar que a conta do usuário não existe