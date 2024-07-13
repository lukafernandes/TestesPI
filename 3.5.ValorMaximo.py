def valorMaximo (quantidadeNumeros: int):
    i = 0
    maiorNumero = 0
    while(i < quantidadeNumeros):
        x = int(input())
        if(x > maiorNumero or i == 0):
            maiorNumero = x
        i += 1
    return maiorNumero

def main():
    quantidadeNumeros = int(input())
    print(valorMaximo(quantidadeNumeros))

main()    