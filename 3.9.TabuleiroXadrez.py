def formarTabuleiro(dimensao: int):
    tabuleiro = ""
    casaBranca = "o"
    casaPreta = "*"    
    for i in range(1, dimensao+1): #i = linha
        linha = ""        
        casa = ""
        if(i%2 != 0):
            for j in range(1, dimensao+1): #j = coluna
                if(j == 1):
                    casa = casaBranca                     
                else:
                    if(casa == casaBranca):
                        casa = casaPreta
                    else:
                        casa = casaBranca
                linha = f"{linha}{casa}"
        else:
            for j in range(1, dimensao+1): #j = coluna
                if(j == 1):
                    casa = casaPreta                     
                else:
                    if(casa == casaBranca):
                        casa = casaPreta
                    else:
                        casa = casaBranca
                linha = f"{linha}{casa}"

        if(i == 1):          
            tabuleiro = f"{tabuleiro}{linha}"
        else:
            tabuleiro = f"{tabuleiro}\n{linha}"

    return tabuleiro

def main():
    dimensao = int(input())
    print(formarTabuleiro(dimensao))

main()
            