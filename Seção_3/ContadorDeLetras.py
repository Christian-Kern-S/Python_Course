frase = input("Insira a frase: ")

verificar_option = True

while verificar_option:
    option = int(input("Escolha uma opção\n\n1 - Contar a quantidade de cada letra\n\n2 - Contar qual letra apareceu mais vezes\n\nOpção: "))
    if option == 1 or option == 2:
        verificar_option = False

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if option == 1:
        print(letra_atual, qtd_apareceu_mais_vezes_atual)
    
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1


if option == 2:
    print(
        'A letra que apareceu mais vezes foi '
        f'"{letra_apareceu_mais_vezes}" que apareceu '
        f'{qtd_apareceu_mais_vezes}x'
    )