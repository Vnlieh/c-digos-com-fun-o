def main ():
    num = int(input("Digite um númeroe:"))
    eh_par(num)

def eh_par(num):
    if num % 2 ==0:
        print("É par")
    else:
        print("É ímpar")

main()