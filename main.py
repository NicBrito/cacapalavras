import cacapalavras
import word_finder
import os

# função principal
def main():
    os.system('cls' if os.name == 'nt' else 'clear') # limpando a tela
    matriz, palavras = cacapalavras.main() # criando o caça-palavras
    word_finder.main(matriz, palavras) # encontrando as palavras

# chamando a função principal
if __name__ == '__main__':
    main()