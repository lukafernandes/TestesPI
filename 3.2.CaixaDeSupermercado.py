def main():
    totalPreco = 0
    totalQuantidade = 0
    quantidade = 100
    while(quantidade != 0):
        quantidade = int(input())
        if(quantidade == 0):
            break
        else:
            preco = float(input())
            totalPreco = totalPreco+(quantidade*preco)
            totalQuantidade = totalQuantidade + quantidade
    if(totalQuantidade == 1):
        print(f"Foi comprado {totalQuantidade} item, totalizando R${totalPreco:.2f}")
    else: 
        print(f"Foram comprados {totalQuantidade} itens, totalizando R${totalPreco:.2f}")

main()