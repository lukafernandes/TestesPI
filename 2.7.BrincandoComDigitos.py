def brincandoComDigitos(numero: int):    
    digito1 = numero//10000
    digito2 = (numero//1000)-(digito1*10)
    digito3 = (numero//100)-(digito1*100)-(digito2*10)
    digito5 = numero%10
    digito4 = ((numero%100)-digito5)/10    
    
    if(numero%2 == 0):        
        resultadoSomaDigitos = int(digito4+digito5)        
    else:
        resultadoSomaDigitos = int(digito1+digito2+digito3)

    if(resultadoSomaDigitos<6):
        return f"{resultadoSomaDigitos}\nA"
    elif(6>=resultadoSomaDigitos<12):
        return f"{resultadoSomaDigitos}\nB"
    else:
        return f"{resultadoSomaDigitos}\nC"
    
def main():
    numero = int(input())

    print(brincandoComDigitos(numero))

main()