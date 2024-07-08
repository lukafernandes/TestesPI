import math

def calcularFracaoMista (numerador: int, denominador: int):
    if(denominador == 0):
        return "ERRO"
    else:
        n = math.floor(numerador/denominador)
        num = numerador%denominador
        den = denominador
        return (f"{n}({num}/{den})")

def main():
    numerador = int(input())
    denominador = int(input())

    print(calcularFracaoMista(numerador, denominador))

main()