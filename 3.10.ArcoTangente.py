def calcularArcoTangente (x: float):
    expoente = 1
    arctan = x
    for i in range(1,100):
        expoente = expoente + 2
        if(i%2 != 0):
            arctan = arctan - ((x**expoente)/expoente)
        else:
            arctan = arctan + ((x**expoente)/expoente)
    return f"{arctan:.3f}"

def main():
    x = float(input())
    print(calcularArcoTangente(x))

main()