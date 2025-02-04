import os

palavra_secreta = input("Insira a palavra secreta: ").lower()
palavra = list(palavra_secreta)

tentativa = 0

_isPalavraCompletra = False

palavra_completa = list(palavra_secreta)
counter = 1

for i in range(len(palavra_completa)):
    palavra_completa[i] = "*"

while(_isPalavraCompletra != True and counter != 0):
    counter = 0
    os.system("cls")
    letra = input('Insira uma letra: ').lower()
    
    for i in range(len(palavra)):
        if letra == palavra[i]:
            palavra_completa[i] = letra
    
    palavra_oculta = ''.join(palavra_completa)
    print("\n",palavra_oculta) 

    for i in range(len(palavra_completa)):
        if palavra_completa[i] != "*" and counter == 0:
            _isPalavraCompletra = True
        else:
            counter += 1
            _isPalavraCompletra = False
    
    input("\nAperte qualquer botão para inserir a próxima letra")
    os.system("cls")
    tentativa += 1

os.system("cls")         
print("Parabéns você completou o jogo\n\nTentativas: ",tentativa)
