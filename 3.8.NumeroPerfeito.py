def numeroPerfeito ():
    x = -1
    while(x != 0):
        x = int(input())
        soma = 0
        if(x == 0):
            break
        else:
            for i in range(1, (x-1)):            
                if(x%i == 0):
                    soma = soma + i
                else:
                    continue
            if(soma == x):
                print(f"{x} é perfeito")
            else:
                print(f"{x} não é perfeito")

def main():
    numeroPerfeito()

main()