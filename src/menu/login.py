import os
from ..word_search.utils import verificar_tentativas_restantes
from ..word_search.words import palavras_finalizar_coleta as finalizar_login
from .login_utils import conta_existe, conta_dados
from .login_menu import main as login_menu

# função para exibir o cabeçalho
def exibir_cabecalho():
    print('''ENTRAR COM UMA CONTA CADASTRADA

Caso queira cancelar o login, digite apenas ENTER.
''') # cabeçalho do menu de login

# função principal
def main():
    tentativas = 3 # definindo a quantidade de tentativas do usuário
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_cabecalho() # exibir cabeçalho do menu de login
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário tiver tentativas
        usuario_nome = input("Nome de usuário: ") # pedindo ao usuário para digitar um nome de usuário para a conta
        if(finalizar_login(usuario_nome)): # caso o usuário queira finalizar o processo de login
            return "Login cancelado" # retornando que o login foi cancelado
        usuario_senha = input("Senha: ") # pedindo ao usuário para digitar uma senha para a conta
        if(finalizar_login(usuario_senha)): # caso o usuário queira finalizar o processo de login
            return "Login cancelado" # retornando que o login foi cancelado
        usuario_conta = {"usuario_nome": usuario_nome, "usuario_senha": usuario_senha} # criando a conta do usuário
        if(conta_existe(usuario_conta)): # se a conta do usuário existir
            print("Login efetuado com sucesso!") # exibir mensagem de sucesso
            return login_menu(conta_dados(usuario_conta)) # chamando a função do menu de login
        else: # se a conta do usuário não existir
            print("Usuário ou senha inválidos! Tente novamente.\n") # exibir mensagem de erro
            tentativas -= 1 # decrementando a quantidade de tentativas