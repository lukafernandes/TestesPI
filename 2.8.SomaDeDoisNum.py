def verifica_soma(a: int, b: int, c:int) -> bool:
    if(a+b == c or a+c == b or b+c == a):
        return "Verdadeiro"
    else:
        return "Falso"
    
def main():
    a = int(input())
    b = int(input())
    c = int(input())

    print(verifica_soma(a,b,c))

main()