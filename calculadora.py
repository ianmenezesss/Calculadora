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
                
def baskara(a,b,c):
    if a == 0:
        return "Não é uma equação de segundo grau"
    delta = ((potencia(b,2)) - 4*a*c)
    if delta < 0:
        return "Não há raizes reais"
    else:
        x1 = (-b + raiz(delta,2))/(2*a)
        x2 = (-b - raiz(delta,2))/(2*a)
        return f"x1 = {x1} , x2 = {x2}"

while True:

    print('-------Menu-------')
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potênciação")
    print("6. Radiciação")
    print("7. Baskara")
    print("0. Sair")

    escolha_operacao = input("Escolha a operação: ")

    try:
        int_escolha = int(escolha_operacao)
    except ValueError:
        print("Digite um numero")
        continue
    else:
        if int_escolha < 0 or int_escolha > 7:
            print("Digite uma operação correta")
        elif int_escolha == 0:
            print("Fim")
            break    
        else:   
            if int_escolha >=1 and int_escolha <= 6:

                x1 = input("Digite o primeiro número: ")

                x2 = input("Digite o segundo número: ")

            elif int_escolha == 7:

                x1 = input("Digite o valor de A: ")

                x2 = input("Digite o valor de B: ")

                x3 = input("Digite o valor de C: ")

            try:
                float_x1 = float(x1)
                float_x2 = float(x2)
                if int_escolha == 7:
                    float_x3 = float(x3)
            except ValueError:
                print("Digite um numero")
            else:
                resultado = None

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
                elif int_escolha == 7:
                    resultado = baskara(float_x1,float_x2,float_x3)
                    print(f"O resultado é : {resultado:}")
                    
