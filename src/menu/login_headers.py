# função para exibir o cabeçalho, caso o usuário não tenha criado nenhum caça-palavras e nenhuma lista de palavras
def cabecalho_1():
    print('''
1- CRIAR NOVO CAÇA-PALAVRAS
2- CRIAR NOVA LISTA DE PALAVRAS
3- SAIR DA CONTA
4- SAIR
0- APAGAR CONTA
''')

# função para exibir o cabeçalho, caso o usuário tenha criado um caça-palavras e nenhuma lista de palavras
def cabecalho_2():
    print('''
1- JOGAR CAÇA-PALAVRAS
2- CRIAR NOVO CAÇA-PALAVRAS
3- VER CAÇA-PALAVRAS SALVOS
4- CRIAR NOVA LISTA DE PALAVRAS
5- SAIR DA CONTA
6- SAIR
0- APAGAR CONTA
''')

# função para exibir o cabeçalho, caso o usuário não tenha criado nenhum caça-palavras, mas tenha criado uma lista de palavras
def cabecalho_3():
    print('''
1- CRIAR NOVO CAÇA-PALAVRAS
2- CRIAR NOVA LISTA DE PALAVRAS
3- VER LISTA DE PALAVRAS SALVAS
4- SAIR DA CONTA
5- SAIR
0- APAGAR CONTA
''')

# função para exibir o cabeçalho, caso o usuário tenha criado um caça-palavras e uma lista de palavras
def cabecalho_4():
    print('''
1- JOGAR CAÇA-PALAVRAS
2- CRIAR NOVO CAÇA-PALAVRAS
3- VER CAÇA-PALAVRAS SALVOS
4- CRIAR NOVA LISTA DE PALAVRAS
5- VER LISTA DE PALAVRAS SALVAS
6- SAIR DA CONTA
7- SAIR
0- APAGAR CONTA
''')

# função para, dinamicamente, receber as opções escolhidas pelo usuário e retornar a ação correspondente
def opcoes_menu(usuario_games, usuario_words, opcao_escolhida):
    if(usuario_games == 0 and usuario_words == 0): # caso o usuário não tenha criado nenhum caça-palavras e nenhuma lista de palavras
        match opcao_escolhida: # verificando a opção escolhida pelo usuário
            case '1': # caso o usuário escolha a opção 1
                return "Criar novo caça-palavras" # retornar que o usuário quer criar um novo caça-palavras
            case '2': # caso o usuário escolha a opção 2
                return "Criar nova lista de palavras" # retornar que o usuário quer criar uma nova lista de palavras
            case '3': # caso o usuário escolha a opção 3
                return "Sair da conta" # retornar que o usuário quer sair da conta
            case '4': # caso o usuário escolha a opção 4
                return "Sair do programa" # retornar que o usuário quer sair do programa
            case '0': # caso o usuário escolha a opção 0
                return "Apagar conta" # retornar que o usuário quer apagar a conta
            case _: # caso o usuário escolha uma opção inválida
                return "Opção inválida" # retornar que a opção escolhida é inválida

    elif(usuario_games != 0 and usuario_words == 0): # caso o usuário tenha criado um caça-palavras e nenhuma lista de palavras
        match opcao_escolhida: # verificando a opção escolhida pelo usuário
            case '1': # caso o usuário escolha a opção 1
                return "JOGAR CAÇA-PALAVRAS" # retornar que o usuário quer jogar um caça-palavras
            case '2': # caso o usuário escolha a opção 2
                return "Criar novo caça-palavras" # retornar que o usuário quer criar um novo caça-palavras
            case '3': # caso o usuário escolha a opção 3
                return "Ver caça-palavras salvos" # retornar que o usuário quer ver os caça-palavras salvos
            case '4': # caso o usuário escolha a opção 4
                return "Criar nova lista de palavras" # retornar que o usuário quer criar uma nova lista de palavras
            case '5': # caso o usuário escolha a opção 5
                return "Sair da conta" # retornar que o usuário quer sair da conta
            case '6': # caso o usuário escolha a opção 6
                return "Sair do programa" # retornar que o usuário quer sair do programa
            case '0': # caso o usuário escolha a opção 0
                return "Apagar conta" # retornar que o usuário quer apagar a conta
            case _: # caso o usuário escolha uma opção inválida
                return "Opção inválida" # retornar que a opção escolhida é inválida

    elif(usuario_games == 0 and usuario_words != 0): # caso o usuário não tenha criado nenhum caça-palavras, mas tenha criado uma lista de palavras
        match opcao_escolhida: # verificando a opção escolhida pelo usuário
            case '1': # caso o usuário escolha a opção 1
                return "Criar novo caça-palavras" # retornar que o usuário quer criar um novo caça-palavras
            case '2': # caso o usuário escolha a opção 2
                return "Criar nova lista de palavras" # retornar que o usuário quer criar uma nova lista de palavras
            case '3': # caso o usuário escolha a opção 3
                return "Ver lista de palavras salvas" # retornar que o usuário quer ver as listas de palavras salvas
            case '4': # caso o usuário escolha a opção 4
                return "Sair da conta" # retornar que o usuário quer sair da conta
            case '5': # caso o usuário escolha a opção 5
                return "Sair do programa" # retornar que o usuário quer sair do programa
            case '0': # caso o usuário escolha a opção 0
                return "Apagar conta" # retornar que o usuário quer apagar a conta
            case _: # caso o usuário escolha uma opção inválida
                return "Opção inválida" # retornar que a opção escolhida é inválida

    else: # caso o usuário tenha criado um caça-palavras e uma lista de palavras
        match opcao_escolhida: # verificando a opção escolhida pelo usuário
            case '1': # caso o usuário escolha a opção 1
                return "JOGAR CAÇA-PALAVRAS" # retornar que o usuário quer jogar um caça-palavras
            case '2': # caso o usuário escolha a opção 2
                return "Criar novo caça-palavras" # retornar que o usuário quer criar um novo caça-palavras
            case '3': # caso o usuário escolha a opção 3
                return "Ver caça-palavras salvos" # retornar que o usuário quer ver os caça-palavras salvos
            case '4': # caso o usuário escolha a opção 4
                return "Criar nova lista de palavras" # retornar que o usuário quer criar uma nova lista de palavras
            case '5': # caso o usuário escolha a opção 5
                return "Ver lista de palavras salvas" # retornar que o usuário quer ver as listas de palavras salvas
            case '6': # caso o usuário escolha a opção 6
                return "Sair da conta" # retornar que o usuário quer sair da conta
            case '7': # caso o usuário escolha a opção 7
                return "Sair do programa" # retornar que o usuário quer sair do programa
            case '0': # caso o usuário escolha a opção 0
                return "Apagar conta" # retornar que o usuário quer apagar a conta
            case _: # caso o usuário escolha uma opção inválida
                return "Opção inválida" # retornar que a opção escolhida é inválida