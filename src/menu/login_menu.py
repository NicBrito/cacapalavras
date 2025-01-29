import os
from ..word_search.utils import verificar_tentativas_restantes
from.utils import usuario_remover

# função para exibir o cabeçalho
def exibir_cabecalho(usuario_nome):
    print(f"BEM-VINDO AO CAÇA-PALAVRAS {usuario_nome.upper()}!\n\n1- APAGAR CONTA\n2- SAIR DA CONTA\n3- SAIR\n") # cabeçalho do menu de login principal

# função principal do menu
def main(usuario_conta):
    tentativas = 3 # definindo a quantidade de tentativas do usuário
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_cabecalho(str(usuario_conta["usuario_nome"])) # exibir cabeçalho do menu de login principal
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário tiver tentativas, ele poderá escolher uma opção
        opcao_escolhida = input("Digite a opção que deseja acessar: ") # opções disponíveis para o usuário
        match opcao_escolhida: # verificando a opção escolhida pelo usuário
            case '1': # caso o usuário escolha a opção 1
                usuario_remover(usuario_conta) # apagando a conta do usuário
                return "Conta apagada" # retornando ao menu principal
            case '2': # caso o usuário escolha a opção 2
                return "Conta deslogada" # retornando ao menu principal
            case '3': # caso o usuário escolha a opção 3
                print("\nFinalizando o programa...") # informando ao usuário que o programa será finalizado
                exit() # finalizando o programa
            case _: # caso o usuário escolha uma opção inválida
                print("Opção inválida! Digite uma opção válida.\n") # informando ao usuário que a opção escolhida é inválida
                tentativas -= 1 # decrementando a quantidade de tentativas