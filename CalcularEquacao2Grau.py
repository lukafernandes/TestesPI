import math

def calcularRaizes(a: float, b: float, c: float):
    delta = (b**2)-(4*a*c)
    if(delta<0):
        print("A equação não possui raízes reais")
    elif(delta==0):
        raiz = (-b+math.sqrt(delta))/(2*a)
        print(f"A raiz é {raiz:,.2f}")
    else:
        raiz1 = (-b-math.sqrt(delta))/(2*a)
        raiz2 = (-b+math.sqrt(delta))/(2*a)
        print(f"As raízes são {raiz1:,.2f} e {raiz2:,.2f}")

def main():
    a = float(input())
    b = float(input())
    c = float(input())

    calcularRaizes(a, b, c)

main()