def reajusteSalarial(salarioAtual: float, tempoServico: int):
    if(salarioAtual<1500):
        salario = salarioAtual+(salarioAtual*0.2)
    elif(1500<=salarioAtual<2000):
        salario = salarioAtual+(salarioAtual*0.15)
    elif(2000<=salarioAtual<6000):
        salario = salarioAtual+(salarioAtual*0.10)
    else:
        salario = salarioAtual
    
    if(tempoServico<1):
        salario = salario
    elif(1<=tempoServico<=3):
        salario = salario+100
    elif(4<=tempoServico<=6):
        salario = salario+200
    elif(7<=tempoServico<=10):
        salario = salario+300
    else:
        salario = salario+500

    if(salario == salarioAtual):
        return "Não houve aumento"
    else:
        return f"O novo salário é R${salario:.2f}"

def main():
    salarioAtual = float(input())
    tempoServico = int(input())

    print(reajusteSalarial(salarioAtual, tempoServico))

main()