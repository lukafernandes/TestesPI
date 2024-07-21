def primoOuNao (n: int):
    for i in range(2, (n//2)):
        if(n%i == 0 and n//i != 1):
            return "Composto"
        else:
            continue
    return "Primo"

def main():
    n = int(input())
    print(primoOuNao(n))

main()