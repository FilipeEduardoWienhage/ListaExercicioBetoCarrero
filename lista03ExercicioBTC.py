import math
import random


def anoBissexto():
    ano = int(input("Digite o ano para saber se é bissexto: "))

    if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
        print(f"Ano informado {ano} é bissexto!")
    else:
        print(f"O ano informado {ano} não é bissexto")


def calculadoraJurosSimples():
    valor = float(input("Digite o valor a ser Calculado: "))
    jurosSimples = float(input("Digite o valor dos Juros ao mês em porcentagem: "))
    tempo = int(input("Digite a quantidade de messes a ser calculado: "))

    taxaJuros = jurosSimples / 100

    juros = valor * taxaJuros * tempo

    totalcomjuros = valor + juros

    print(f"Juros calculado foi de R$: {juros:.2f}")
    print(f"Valor total com juros somados R$: {totalcomjuros:.2f}")


def conversorNumerosRomanos():
    numero = int(input("Digite um número inteiro para converter para romano: "))

    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    resultado = ""

    for i in range(len(valores)):
        while numero >= valores[i]:
            numero -= valores[i]
            resultado += simbolos[i]

    print(f"O número em romano é: {resultado}")


def numerosPrimos():
    numero = int(input("Digite um número para verificar se é um número primo ou não: "))

    if numero <= 1:
        print(f"{numero} não é um número primo.")
        return


    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            return 

    print(f"{numero} é um número primo!")


def calculadoraMediaDesvioPadrao():
    numeros = [13, 27, 31, 44, 52, 22, 21, 56, 99, 14]
    
    media = sum(numeros) / len(numeros)
    
    variancia = sum((num - media) ** 2 for num in numeros) / len(numeros)
    desvio_padrao = math.sqrt(variancia)
    
    print(f"Números: {numeros}")
    print(f"Média: {media}")
    print(f"Desvio Padrão: {desvio_padrao}")


def jogoForcaSimples():
    palavras = ["python", "desenvolvimento", "programacao", "artificial", "inteligencia", "java", "dados", "oloko"]
    palavra = random.choice(palavras)
    palavra_oculta = ["_"] * len(palavra)

    while True:
        print("\n" + " ".join(palavra_oculta))
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            print(f"A letra '{letra}' não está na palavra.")

        if "_" not in palavra_oculta:
            print(f"Você Acertou! A palavra era: {palavra}")
            break


#anoBissexto()
#calculadoraJurosSimples()
#conversorNumerosRomanos()
#numerosPrimos()
#calculadoraMediaDesvioPadrao()
#jogoForcaSimples()

