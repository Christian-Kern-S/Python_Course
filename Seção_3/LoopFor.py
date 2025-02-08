lista = []  # Inicializa a lista uma única vez

# Primeiro loop (coleta de dados)
for _ in range(10):  # O "_" é uma variável anônima (não precisamos do "i")
    numero = int(input("Número: "))  # Converte para inteiro
    lista.append(numero)  # Adiciona à lista

# Segundo loop (exibição)
for elemento in lista:  # Itera diretamente pela lista
    print(elemento)