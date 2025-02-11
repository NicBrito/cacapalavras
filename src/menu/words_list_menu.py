import os
from ..word_search.utils import verificar_tentativas_restantes
from .words_list_utils import exibir_listas_palavras, salvar_lista_palavras, criar_lista_palavras, remover_lista_palavras, editar_lista_palavras
from .login_utils import conta_atualizar

# função para exibir o menu de listas de palavras
def menu_ver_lista_palavras():
    print('''1- CRIAR NOVA LISTA DE PALAVRAS
2- EDITAR UMA LISTA DE PALAVRAS
3- REMOVER UMA LISTA DE PALAVRAS
4- VOLTAR
''')

# função para verificar as opções do menu de listas de palavras
def opcoes_menu():
    opcao_escolhida = input("Digite a opção que deseja acessar: ") # opções disponíveis para o usuário
    match opcao_escolhida: # verificando a opção escolhida pelo usuário
        case '1': # caso o usuário escolha a opção "Criar nova lista de palavras"
            return 'Criar nova lista de palavras' # retornando a ação correspondente à opção escolhida
        case '2': # caso o usuário escolha a opção "Editar uma lista de palavras"
            return 'Editar uma lista de palavras' # retornando a ação correspondente à opção escolhida
        case '3': # caso o usuário escolha a opção "Remover uma lista de palavras"
            return 'Remover uma lista de palavras' # retornando a ação correspondente à opção escolhida
        case '4': # caso o usuário escolha a opção "Voltar"
            return 'Voltar' # retornando a ação correspondente à opção escolhida
        case _: # caso o usuário escolha uma opção inválida
            return 'Opção inválida' # retornando a ação correspondente à opção escolhida

# função principal
def main(usuario_conta, acao_escolhida):
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    tentativas = 3 # definindo a quantidade de tentativas do usuário
    while(verificar_tentativas_restantes(tentativas)): # enquanto o usuário não sair do menu
        match acao_escolhida: # verificando a ação escolhida pelo usuário
            case 'Criar nova lista de palavras': # caso o usuário escolha a opção "Criar nova lista de palavras"
                lista_palavras = criar_lista_palavras(usuario_conta) # criando uma nova lista de palavras
                if(lista_palavras): # caso a lista de palavras seja criada
                    salvar_lista_palavras(usuario_conta, lista_palavras) # salvando a nova lista de palavras
                    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                    print("Lista de palavras criada com sucesso!\n") # informando ao usuário que a lista de palavras foi criada
                    conta_atualizar(usuario_conta, "adicionar listas_palavras") # atualizando a quantidade de listas de palavras
                    return # finalizando a criação da lista de palavras
                else: # caso a lista de palavras não seja criada
                    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                    print("Lista de palavras não criada!\n") # informando ao usuário que a lista de palavras não foi criada
                    return # finalizando a criação da lista de palavras
            case 'Ver lista de palavras salvas': # caso o usuário escolha a opção "Ver lista de palavras salvas"
                exibir_listas_palavras(usuario_conta) # exibindo a lista de palavras salvas
                menu_ver_lista_palavras() # exibindo o menu de listas de palavras
                acao_escolhida = opcoes_menu() # retornando a ação correspondente à opção escolhida
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
            case 'Editar uma lista de palavras': # caso o usuário escolha a opção "Editar uma lista de palavras"
                retorno_editar_lista = False # definindo valor inicial para a edição da lista de palavras
                while(True): # enquanto o usuário não sair do menu
                    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                    exibir_listas_palavras(usuario_conta) # exibindo a lista de palavras salvas
                    if(retorno_editar_lista == 'Lista editada'): # caso a lista de palavras seja editada
                        print("Lista de palavras editada com sucesso!\n") # informando ao usuário que a lista de palavras foi editada
                    elif(retorno_editar_lista == 'Lista não encontrada'): # caso a lista de palavras não seja encontrada
                        print("Lista de palavras não encontrada!\n") # informando ao usuário que a lista de palavras não foi encontrada
                    elif(retorno_editar_lista == 'Lista vazia'): # caso a lista de palavras esteja vazia
                        print("Lista de palavras apagada!\n") # informando ao usuário que a lista de palavras foi apagada
                        conta_atualizar(usuario_conta, "remover listas_palavras") # atualizando a quantidade de listas de palavras
                    elif(retorno_editar_lista == 'Cancelar edição'): # caso a edição da lista de palavras seja cancelada
                        os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                        acao_escolhida = 'Ver lista de palavras salvas' # retornando à lista de palavras salvas
                        break # finalizando a edição da lista de palavras
                    if(usuario_conta["listas_palavras"] == 0): # caso o usuário não tenha listas de palavras salvas
                        os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                        return "Listas apagadas" # retornando que as listas de palavras foram apagadas
                    print("EDITAR LISTA DE PALAVRAS\n"
                          "\nPara cancelar, digite ENTER\n") # informando ao usuário que a edição de uma lista de palavras foi iniciada
                    retorno_editar_lista = editar_lista_palavras(usuario_conta) # editando uma lista de palavras
            case 'Remover uma lista de palavras': # caso o usuário escolha a opção "Remover uma lista de palavras"
                retorno_remover_lista = False # definindo valor inicial para a remoção da lista de palavras
                while(True): # enquanto o usuário não sair do menu
                    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                    exibir_listas_palavras(usuario_conta) # exibindo a lista de palavras salvas
                    if(retorno_remover_lista == 'Lista removida'): # caso a lista de palavras seja removida
                        print("Lista de palavras removida com sucesso!\n") # informando ao usuário que a lista de palavras foi removida
                        conta_atualizar(usuario_conta, "remover listas_palavras") # atualizando a quantidade de listas de palavras
                    elif(retorno_remover_lista == 'Lista não encontrada'): # caso a lista de palavras não seja encontrada
                        print("Lista de palavras não encontrada!\n") # informando ao usuário que a lista de palavras não foi encontrada
                    elif(retorno_remover_lista == 'Cancelar remoção'): # caso a remoção da lista de palavras seja cancelada
                        os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                        acao_escolhida = 'Ver lista de palavras salvas' # retornando à lista de palavras salvas
                        break # finalizando a remoção da lista de palavras
                    if(usuario_conta["listas_palavras"] == 0): # caso o usuário não tenha listas de palavras salvas
                        os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                        return "Listas apagadas" # retornando que as listas de palavras foram apagadas
                    print("REMOVER LISTA DE PALAVRAS\n"
                        "\nPara cancelar, digite ENTER\n") # informando ao usuário que a remoção de uma lista de palavras foi iniciada e como cancelar
                    retorno_remover_lista = remover_lista_palavras(usuario_conta) # removendo uma lista de palavras
            case 'Voltar': # caso o usuário escolha a opção "Voltar"
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                return # retornando ao menu principal
            case 'Opção inválida': # caso o usuário escolha a opção "Opção inválida"
                tentativas -= 1 # decrementando a quantidade de tentativas
                os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
                exibir_listas_palavras(usuario_conta) # exibindo a lista de palavras salvas
                menu_ver_lista_palavras() # exibindo o menu de listas de palavras
                print("Opção inválida! Digite uma opção válida.\n") # informando ao usuário que a opção escolhida é inválida
                if(tentativas != 0): # caso o usuário ainda tenha tentativas
                    acao_escolhida = opcoes_menu() # retornando a ação correspondente à opção escolhida