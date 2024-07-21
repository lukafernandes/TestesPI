def crescenteOuNao(n: int):
    x = 0
    y = 0
    for i in range(n):
        x = int(input())
        if(x > y or i == 0):
            y = x
            
    if(x == y):
        return "Crescente"
    else:
        return "Não crescente"
    
def main():
    n = int(input())
    
    print(crescenteOuNao(n))
    
main()