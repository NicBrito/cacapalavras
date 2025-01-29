import os
from src.menu.main_menu import main as menu

# função principal
def main():
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    menu() # chamando o menu

# chamando a função principal
if __name__ == '__main__':
    main()