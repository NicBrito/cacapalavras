import os
from ..word_search.utils import verificar_tentativas_restantes
from .login_headers import cabecalho_1, cabecalho_2, cabecalho_3, cabecalho_4, opcoes_menu
from .login_utils import conta_apagar, conta_apagar_dados, conta_carregar_dados, usuario_possui_dados
from .words_list_menu import main as words_list_menu
from .words_list_utils import contar_listas_palavras

# função para exibir o cabeçalho
def exibir_cabecalho(usuario_nome, cacapalavras_salvos, listas_palavras):
    print(f"BEM-VINDO AO CAÇA-PALAVRAS {usuario_nome.upper()}!") # cabeçalho do menu de login principal
    if(cacapalavras_salvos == 0 and listas_palavras == 0): # caso o usuário não tenha criado nenhum caça-palavras e nenhuma lista de palavras
        cabecalho_1() # exibir cabeçalho 1
    elif(cacapalavras_salvos != 0 and listas_palavras == 0): # caso o usuário tenha criado um caça-palavras e nenhuma lista de palavras
        cabecalho_2() # exibir cabeçalho 2
    elif(cacapalavras_salvos == 0 and listas_palavras != 0): # caso o usuário não tenha criado nenhum caça-palavras, mas tenha criado uma lista de palavras
        cabecalho_3() # exibir cabeçalho 3
    else: # caso o usuário tenha criado um caça-palavras e uma lista de palavras
        cabecalho_4() # exibir cabeçalho 4

# função principal do menu
def main(usuario_conta):
    if(usuario_possui_dados(usuario_conta)): # caso o usuário possua dados salvos
        cacapalavras_salvos = usuario_conta["cacapalavras_salvos"] # obtendo a quantidade de caça-palavras salvos
        listas_palavras = contar_listas_palavras(usuario_conta) # contando as listas de palavras
        dados = {"cacapalavras_salvos": cacapalavras_salvos,
                 "listas_palavras": listas_palavras} # definindo os dados do usuário
        conta_carregar_dados(usuario_conta, dados) # carregando os dados do usuário
    tentativas = 3 # definindo a quantidade de tentativas do usuário
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    exibir_cabecalho(usuario_conta["usuario_nome"], usuario_conta["cacapalavras_salvos"], usuario_conta["listas_palavras"]) # exibir cabeçalho do menu de login principal
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário tiver tentativas, ele poderá escolher uma opção
        opcao_escolhida = input("Digite a opção que deseja acessar: ") # solicitando ao usuário que escolha uma opção
        acao_retornada = opcoes_menu(usuario_conta["cacapalavras_salvos"], usuario_conta["listas_palavras"], opcao_escolhida) # retornando a ação correspondente à opção escolhida
        match acao_retornada: # verificando a ação retornada
            case 'JOGAR CAÇA-PALAVRAS': # caso o usuário escolha a opção "JOGAR CAÇA-PALAVRAS"
                pass
            case 'Criar novo caça-palavras': # caso o usuário escolha a opção "Criar novo caça-palavras"
                pass
            case 'Ver caça-palavras salvos': # caso o usuário escolha a opção "Ver caça-palavras salvos"
                pass
            case 'Criar nova lista de palavras': # caso o usuário escolha a opção "Criar nova lista de palavras"
                words_list_menu(usuario_conta, acao_retornada) # acessando o menu de listas de palavras
            case 'Ver lista de palavras salvas': # caso o usuário escolha a opção "Ver lista de palavras salvas"
                if(words_list_menu(usuario_conta, acao_retornada) == "Listas apagadas"): # caso não haja listas de palavras salvas
                    print("Todas as listas de palavras foram apagadas!\n") # informando ao usuário que todas as listas de palavras foram apagadas
                    conta_apagar_dados(usuario_conta) # apagando os dados da conta do usuário
            case 'Sair da conta': # caso o usuário escolha a opção "Sair da conta"
                return "Conta deslogada" # retornando ao menu principal
            case 'Sair do programa': # caso o usuário escolha a opção "Sair do programa"
                print("\nFinalizando o programa...") # informando ao usuário que o programa será finalizado
                exit() # finalizando o programa
            case 'Apagar conta': # caso o usuário escolha a opção "Apagar conta"
                retorno_apagar_conta = conta_apagar(usuario_conta) # apagando a conta do usuário
                if(retorno_apagar_conta == "Conta e dados apagados"): # caso a conta e os dados do usuário sejam apagados
                    return "Conta e dados apagados" # retornando ao menu principal
                elif(retorno_apagar_conta == "Conta apagada, dados mantidos"): # caso a conta seja apagada, mas os dados do usuário sejam mantidos
                    return "Conta apagada, dados mantidos" # retornando ao menu principal
                elif(retorno_apagar_conta == "Conta apagada"): # caso a conta seja apagada e não haja dados do usuário
                    return "Conta apagada" # retornando ao menu principal
            case 'Opção inválida': # caso o usuário escolha a opção "Opção inválida"
                print("Opção inválida! Digite uma opção válida.\n") # informando ao usuário que a opção escolhida é inválida
                tentativas -= 1 # decrementando a quantidade de tentativas
                continue # solicitando ao usuário que escolha uma nova opção
        exibir_cabecalho(usuario_conta["usuario_nome"], usuario_conta["cacapalavras_salvos"], usuario_conta["listas_palavras"]) # exibir cabeçalho do menu de login principal