import os

os.system("cls")
input("Bem-vindo ao Kern Markert!\n\nPara acessar o menu de supervisor, aperte 'Enter'.")
os.system("cls")

opcao = "1"
lista = []

while(opcao != 0):
    opcao = input("Menu Supervisor\n\nSelecione uma opção:\n(I)nserir (A)pagar (L)istar (S)air\n\nOpção: ").lower()
    os.system("cls")
    if(opcao == "s"):
        opcao = 0
    elif(opcao != "i" and opcao != "a" and opcao != "l"):
        input("Opção invalida, selecione novamente!\n\nPrecione 'Enter' para continuar")
        os.system("cls")
        continue
    
    match opcao:
        case "i":
            novoProduto = input("Insira o nome do produto: ")
            try:
                lista.append(novoProduto)
                print("Produto inserido com sucesso")
            except ValueError:
                print("Não foi possível inserir o produto")
                
            input("\nPrecione 'Enter' para continuar")
            os.system("cls")
            
        case "a":
            indice = int(input("infome o número do produto: "))
            try:
                del lista[indice]
                print("Produto removido com sucesso")
            except IndexError:
                print("Não foi possível remover o produto")
                
            input("\nPrecione 'Enter' para continuar")
            os.system("cls")
            
        case "l":
            print("Lista de produtos\n")
            
            try:
                for indice, produto in enumerate(lista):
                    print(indice, produto)
                
            except:
                print("Não há produtos a serem listados")    
            
            input("\nPrecione 'Enter' para continuar")
            os.system("cls")
