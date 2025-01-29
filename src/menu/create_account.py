import os
from ..word_search.utils import verificar_tentativas_restantes
from ..word_search.words import palavras_finalizar_coleta as finalizar_cadastro
from .utils import usuario_existe, usuario_salvar

# função para exibir o cabeçalho
def exibir_cabecalho():
    print('''CADASTRAR NOVA CONTA

Caso queira cancelar o cadastro, digite apenas ENTER.
''') # cabeçalho do menu de cadastro

# função principal
def main():
    tentativas = 3 # definindo a quantidade de tentativas do usuário
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_cabecalho() # exibir cabeçalho do menu de cadastro
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário tiver tentativas
        usuario_nome = input("Digite um nome de usuário: ") # pedindo ao usuário para digitar um nome de usuário para a conta
        if(finalizar_cadastro(usuario_nome)): # caso o usuário queira finalizar o processo de cadastro
            return # finalizando o processo de cadastro
        if(usuario_existe(usuario_nome)): # se o nome de usuário já existir
            print("O nome de usuário já está em uso! Digite um nome de usuário válido.\n") # informando que o nome de usuário já está em uso
            tentativas -= 1 # decrementando a quantidade de tentativas
            continue # pedir ao usuário para digitar um nome de usuário novamente
        else: # se o nome de usuário não existir
            break # continuar com o cadastro
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário tiver tentativas
        usuario_senha = input("Digite uma senha: ") # pedindo ao usuário para digitar uma senha para a conta
        if(finalizar_cadastro(usuario_senha)): # caso o usuário queira finalizar o processo de cadastro
            return False # informando que o usuário não foi cadastrado
        senha_repetida = input("Digite a senha novamente: ") # pedindo ao usuário para digitar a senha novamente
        if(senha_repetida == usuario_senha): # se a senha repetida for igual a senha criada
            break # continuar com o cadastro
        else: # se a senha repetida for diferente da senha criada
            print("A senhas digitadas são diferentes! Digite as senhas novamente.\n") # exibir mensagem de erro
            tentativas -= 1 # decrementando a quantidade de tentativas
    usuario_conta = {"usuario_nome": usuario_nome, "usuario_senha": usuario_senha} # criando a conta do usuário
    usuario_salvar(usuario_conta) # salvando a conta do usuário no arquivo
    return True # informando que o usuário foi cadastrado