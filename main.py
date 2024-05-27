import cacapalavras

# função principal
def main():
    matriz, palavras = cacapalavras.main() # chamando a função main do módulo cacapalavras
    cacapalavras.exibir_matriz(matriz) # printando a matriz
    cacapalavras.exibir_palavras(palavras) # printando as palavras

# chamando a função principal
if __name__ == '__main__':
    main()