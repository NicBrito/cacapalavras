import os
from core import main as create_word_search
from finder import main as finding_words

# função principal
def main():
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    matriz, palavras = create_word_search() # criando o caça-palavras
    finding_words(matriz, palavras) # encontrando as palavras

# chamando a função principal
if __name__ == '__main__':
    main()