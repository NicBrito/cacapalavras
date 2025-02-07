import os
from ..word_search.utils import verificar_tentativas_restantes
from .create_account import main as criar_conta
from .login import main as login

# função para exibir o cabeçalho
def exibir_cabecalho():
    print('''BEM-VINDO AO CAÇA-PALAVRAS!

1- CRIAR CONTA
2- FAZER LOGIN
3- SAIR
''') # cabeçalho do menu principal

# função principal do menu
def main():
    tentativas = 3 # definindo a quantidade de tentativas do usuário
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_cabecalho() # exibir cabeçalho do menu principal
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário tiver tentativas, ele poderá escolher uma opção
        opcao_escolhida = input("Digite a opção que deseja acessar: ") # opções disponíveis para o usuário
        match opcao_escolhida: # verificando a opção escolhida pelo usuário
            case '1': # caso o usuário escolha a opção 1
                retorno_criar_conta = criar_conta() # chamando a função para criar uma conta
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                if(retorno_criar_conta): # caso a conta seja criada
                    print("Conta criada com sucesso.\n") # informando que a conta foi criada com sucesso
                else: # caso o cadastro seja cancelado
                    print("Cadastro cancelado!\n") # informando que o cadastro foi cancelado
            case '2': # caso o usuário escolha a opção 2
                retorno_login = login() # chamando a função para fazer login
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                match retorno_login: # verificando o retorno da função de login
                    case "Login cancelado": # caso o login seja cancelado
                        print("Login cancelado!\n") # informando que o login foi cancelado
                    case "Conta deslogada": # caso a conta seja deslogada
                        print("Conta deslogada!\n") # informando que a conta foi deslogada
                    case "Conta e dados apagados": # caso a conta e os dados sejam apagados
                        print("Conta e dados apagados!\n") # informando que a conta e os dados foram apagados
                    case "Conta apagada, dados mantidos": # caso a conta seja apagada, mas os dados sejam mantidos
                        print("Conta apagada, dados mantidos!\n") # informando que a conta foi apagada, mas os dados foram mantidos
                    case "Conta apagada": # caso a conta seja apagada e não haja dados
                        print("Conta apagada!\n") # informando que a conta foi apagada
            case '3': # caso o usuário escolha a opção 3
                print("\nFinalizando o programa...") # informando ao usuário que o programa será finalizado
                exit() # finalizando o programa
            case _: # caso o usuário escolha uma opção inválida
                print("Opção inválida! Digite uma opção válida.\n") # informando ao usuário que a opção escolhida é inválida
                tentativas -= 1 # decrementando a quantidade de tentativas
                continue # solicitando uma nova entrada do usuário
        exibir_cabecalho() # exibir cabeçalho do menu principal