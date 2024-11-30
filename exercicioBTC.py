import os
import time


def calcule_imc():
    while True:
        try: 
            peso = float(input("Digite seu peso (em kg): "))
            if peso > 0:
                break
            else:
                print("Peso não pode ser 0")
        except ValueError:
            print("Por favor, verifique o dado inserido")
    while True:
        try:
            altura = float(input("Digite sua altura (em metros): "))
            if 0.5 <= altura <= 3.0:
                break
            else:
                print("Insira a altura entre 0.5 e 3.0 Metros")
        except ValueError:
            print("Por favor, verifique o dado inserido")

    imc = peso / (altura ** 2)  
    
    print(f"Seu IMC é: {imc:.2f}")  
    
    if imc < 17:
        print("Muito abaixo do peso")
    elif 17 <= imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc < 30:
        print("Acima do peso")
    elif 30 <= imc < 35:
        print("Obesidade I")
    elif 35 <= imc <= 40:
        print("Obesidade II")
    else: 
        print("Obesidade mórbida")


def conversorTemperatura():
    while True:
        print("\n Conversor de Temperatura")
        print("1- Graus Celsius para Fahrenheit")
        print("2- Fahrenheit para Graus Celsius")
        print("3- Sair")

        escolha = input("Escolha uma das Opções: ")

        if escolha == "1": 
            try: 
                celsius = float(input("Digite a temperatura em Celsius: "))
                fahrenheit = (celsius * 1.8) + 32
                print(f"A Temperatura em Fahrenheit é: {fahrenheit:.2f}ºF")
            except ValueError:
                print("Por favor, insira um numero válido")

        elif escolha == "2":
            try:
                fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
                celsius = (fahrenheit - 32) / 1.8
                print(f"A temperatura em Graus Celsius é: {celsius:.2f}ºC")
            except ValueError:
                print("Por favor, insira um numero válido")
        
        elif escolha == "3":
            print("Até a próxima")
            break

        else: 
            print("Opção Inválida")


def contadorPalavras():
    caminho_arquivo = "C:/Users/filip/Documents/GitHub/ListaExercicioBetoCarrero/contarPalavras.txt"

    if os.path.exists(caminho_arquivo):
    
        with open(caminho_arquivo) as arquivo:
            ler = arquivo.read()
            palavras = ler.split()
            contarPalavras = len(palavras) 
            print(ler)      
            print(f'O número de palavras no arquivo é: {contarPalavras}')

    else:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')


#geradorListaCompras()
#contadorPalavras()
# conversorTemperatura()
# calcule_imc()