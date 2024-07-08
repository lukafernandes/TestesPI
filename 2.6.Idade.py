def podeVotarDirigir(ano: int, nacionalidade: str):
    idade = 2024 - ano
    if(nacionalidade == "brasileira"):
        if(idade<16):
            return f"Você tem {idade} anos"
        elif(16<=idade<18):
            return f"Você tem {idade} anos\nJá pode votar"
        else:
            return f"Você tem {idade} anos\nJá pode votar\nJá pode solicitar a Carteira de Habilitação"
    else:
        return f"Você tem 34 anos\nVerifique as regras do país onde você vota e/ou pretende tirar carteira de habilitação"
    
def main():
    ano = int(input())
    nacionalidade = input()

    print(podeVotarDirigir(ano, nacionalidade))

main()