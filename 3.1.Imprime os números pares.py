def numerosPares (x: int):
    i = 1
    while i<=x:
        if(i%2 == 0):
            print(i)
        i += 1

def main():
    x= int(input())

    numerosPares(x)

main()