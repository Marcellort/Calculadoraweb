from calc import soma, divisao
historico=[]
operando= True
while (operando):
    number1= float(input("Digite o primerio valor: "))
    opcao= input("Digite a operação que deseja realizar, Ex para soma +, Para sair digite qualquer valor")
    number2= float(input("Digite o segundo valor"))
    if opcao == '+':
        resultado = soma(number1,number2)
        print(f"O resultado da soma é {resultado:.2f}: ")
    elif opcao == '-':
        resultado = subtracao(number1,number2)
        print(f"O resultado da subtração é {resultado:.2f}: ")
    elif opcao == '*':
        resultado = multiplicacao(number1,number2)
        print(f"O resultado da subtração é {resultado:.2f}: ")
    elif opcao == '/':
        resultado = divisao(number1,number2)
        print(f"O resultado da subtração é {resultado:.2f}: ")
    else:
        print("Até mais")
        operando= False

