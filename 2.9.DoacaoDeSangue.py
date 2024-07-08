def verificarCompatibilidade(idadeDoador: int, pesoDoador: float, tipoSanguineoDoador: str, rhDoador: str,tipoSanguineoReceptor: str, rhReceptor: str ):
    if(idadeDoador<16 or pesoDoador<50):
        return "Doador não satisfaz requisitos mínimos"
    else:
        if(rhDoador=="+" and rhReceptor=="-"):           
            return "Tipos sanguíneos incompatíveis"
        else:
            if(tipoSanguineoReceptor=="A" and (tipoSanguineoDoador=="A" or tipoSanguineoDoador=="O")):
                return "Tipos sanguíneos compatíveis"
            elif(tipoSanguineoReceptor=="B" and (tipoSanguineoDoador=="B" or tipoSanguineoDoador=="O")):
                return "Tipos sanguíneos compatíveis"
            elif(tipoSanguineoReceptor=="AB" and (tipoSanguineoDoador=="A" or tipoSanguineoDoador=="B" or tipoSanguineoDoador=="AB" or tipoSanguineoDoador=="O")):
                return "Tipos sanguíneos compatíveis"
            elif(tipoSanguineoReceptor=="O" and tipoSanguineoDoador=="O"):
                return "Tipos sanguíneos compatíveis"
            else:
                return "Tipos sanguíneos incompatíveis"

def main():
   idadeDoador = int(input())
   pesoDoador = float(input())
   tipoSanguineoDoador = input()
   rhDoador = input()
   tipoSanguineoReceptor = input()
   rhReceptor = input()

   print(verificarCompatibilidade(idadeDoador, pesoDoador, tipoSanguineoDoador, rhDoador, tipoSanguineoReceptor, rhReceptor))

main()