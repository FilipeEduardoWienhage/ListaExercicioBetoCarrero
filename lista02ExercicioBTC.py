import random
import string


def geradorSenhas():
    caracteres = string.ascii_letters + string.digits + string.punctuation

    tamanhoSenha = int(input("Digite a quantidade de caracteres qua a senha deve conter: "))

    senha = ''.join(random.choice(caracteres) for i in range(tamanhoSenha))

    print(f"Sua senha gerada foi: {senha}")


def contadorVogaisConsoantes():
    vogais = "aeiou"
    contador_vogais = 0
    contador_consoantes = 0

    texto = input("Digite uma palavra, frase ou texto: ").lower()

    for caractere in texto:
        if caractere in vogais:
            contador_vogais += 1
        elif 'a' <= caractere <= 'z': 
            contador_consoantes += 1
        
    print(f"Existem: {contador_vogais} vogais e {contador_consoantes} consoantes.")


def advinhaNumero():
    numeroAleatorio = random.randint(1,20)
    tentativas = 0
    while True:
        try:
            numeroEscolhido = int(input("Digite um número de 1 a 20: "))
            tentativas += 1
            if numeroEscolhido < numeroAleatorio:
                print("O número é maior que seu palpite")
            elif numeroEscolhido > numeroAleatorio:
                print("O número é menor que o palpite")
            else:
                print(f"Você acertou o número aleatorio {numeroAleatorio} em {tentativas} tentativas")
                break
        except ValueError:
            print("Por favor, digite um número válido")                


def calculadora():
    while True:
        print("\n Calculadora")
        print("1- Somar")
        print("2- Subtrair")
        print("3- Multiplicar")
        print("4- Dividir")
        print("5- Sair")

        escolha = input("Escolha uma das Opções: ")

        if escolha == "1":
            valor1 = int(input("Digite o Primeiro Número: "))
            valor2 = int(input("Digite o Segundo Número: "))
            resultado = valor1 + valor2
            print("O Resultado é: ", resultado)

        elif escolha == "2":
            valor1 = int(input("Digite o Primeiro Número: "))
            valor2 = int(input("Digite o Segundo Número: "))
            resultado = valor1 - valor2
            print("O Resultado é: ", resultado)
        
        elif escolha == "3":
            valor1 = int(input("Digite o Primeiro Número: "))
            valor2 = int(input("Digite o Segundo Número: "))
            resultado = valor1 * valor2
            print("O Resultado é: ", resultado)

        elif escolha == "4":
            valor1 = int(input("Digite o Primeiro Número: "))
            valor2 = int(input("Digite o Segundo Número: "))
            if valor2 == 0:
                print("Valor inválido")
                break
            resultado = valor1 / valor2           
            print("O Resultado é: ", resultado)

        elif escolha == "5":
            print("Obrigado por utilizar a função")
            break

        else:
            print("Opção Inválida")


def verificaPalindromos():
    texto = input("Digite uma palavra ou frase: ")
    
    textoTratado = ''.join(caractere.lower() for caractere in texto if caractere.isalnum())
    
    if textoTratado == textoTratado[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


#geradorSenhas()
#contadorVogaisConsoantes()
#advinhaNumero()
#calculadora()
verificaPalindromos()