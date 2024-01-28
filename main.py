# fazer lista com as palavras que devem ser encontradas
palavras = ["amor", "paz", "raiva", "python", "lar"]

# criando as linhas da matriz
lista1 = ['a', 'b', 'c', 'd', 'e', 'f']
lista2 = ['a', 'b', 'c', 'd', 'e', 'f']
lista3 = ['a', 'b', 'c', 'd', 'e', 'f']
lista4 = ['a', 'b', 'c', 'd', 'e', 'f']
lista5 = ['a', 'b', 'c', 'd', 'e', 'f']
lista6 = ['a', 'b', 'c', 'd', 'e', 'f']

# criando a matriz utilizando as listas
matriz = [
    lista1,
    lista2,
    lista3,
    lista4,
    lista5,
    lista6
]

# colocando as palavras na matriz
linha_matriz = 0
for palavra in palavras:
    coluna_matriz = 0
    for letra in palavra:
        matriz[linha_matriz][coluna_matriz] = letra
        coluna_matriz += 1
    linha_matriz += 1

# pritando a matriz
for x in matriz:
    print(x)