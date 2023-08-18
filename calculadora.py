print('-------Menu-------')
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potênciação")
print("6. Radiciação")

escolha_operacao = input("Escolha a operação: ")

try:
    int_escolha = int(escolha_operacao)
except ValueError:
    print("Digite um numero")
else:
    if int_escolha < 1 or int_escolha > 6:
        print("Digite uma operação correta")
    else:

        def soma(x, y):
            return x + y

        def subtracao(x, y):
            return x - y

        def multiplicacao(x, y):
            return x * y

        def divisao(x, y):
            if y != 0:
                return x / y
            else:
                return "Não é Possivel Dividir por Zero"
            
        def potencia(x,y):
            return x ** y
        
        def raiz(x,y):
            if y != 0:
                return x ** (1/y)
            else:
                return "Não é Possivel Radiciar por Zero"

        x1 = input("Digite o primeiro número: ")

        x2 = input("Digite o segundo número: ")

        try:
            float_x1 = float(x1)
            float_x2 = float(x2)
        except ValueError:
            print("Digite um numero")
        else:
            resultado = None

            if int_escolha >= 1 and int_escolha <= 6:
                if int_escolha == 1:
                    resultado = soma(float_x1,float_x2)
                    print(f"O resultado é : {resultado:}")
                elif int_escolha == 2:
                    resultado = subtracao(float_x1,float_x2)
                    print(f"O resultado é : {resultado:}")
                elif int_escolha == 3:
                    resultado = multiplicacao(float_x1,float_x2)
                    print(f"O resultado é : {resultado:}")
                elif int_escolha == 4:
                    resultado = divisao(float_x1,float_x2)
                    print(f"O resultado é : {resultado:}")
                elif int_escolha == 5:
                    resultado = potencia(float_x1,float_x2)
                    print(f"O resultado é : {resultado:}")
                elif int_escolha == 6:
                    resultado = raiz(float_x1,float_x2)
                    print(f"O resultado é : {resultado:}")
            else:
                print("Digite um número de Operação")

