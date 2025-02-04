import os

def switch_case(option):
        match option:
                case 1:
                        return print("\nSoma:",n1+n2)
                case 2:
                        return print("\nSubtração:",n1-n2)
                case 3:
                        return print("\nMultipicação:",n1*n2)
                case 4:
                        return print("\nDivisão:",n1/n2)
                case 0:
                        return exit
                case _:
                        return print("\nOpção incorreta, selecione novamente")

op = 1
while(op != 0):
        n1 = int(input("Insira o primeiro número: "))
        os.system("cls")
        n2 = int(input("Insira o segundo número: "))
        os.system("cls")
        op = int(input("Selecione o tipo de calculo\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n\nOpção: "))
        os.system("cls")
        switch_case(op)
        input("\nPressione Enter para continuar...")
        os.system("cls")
