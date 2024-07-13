def numeroDigitos(x: int):
    numeroDigitos = 0
    while(x > 0):
        x = x//10
        numeroDigitos += 1
    return numeroDigitos

def main():
    x = int(input())
    print(numeroDigitos(x))

main()