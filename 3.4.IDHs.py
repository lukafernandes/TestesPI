def classificacaoIDHs (idh: float):    
    if(idh > 0.80):
        classificacao = "muito alto"
    elif(0.70 < idh <= 0.80):
        classificacao = "alto"
    elif(0.55 <= idh <= 0.70):
        classificacao = "médio"
    else:
        classificacao = "baixo"
    
    return classificacao

def main():
    quantidadePaises = int(input())
    i = 0
    while(i < quantidadePaises):
        pais = input()
        idh = float(input())
        print(f"{pais} tem IDH {classificacaoIDHs(idh)}")
        i += 1

main()