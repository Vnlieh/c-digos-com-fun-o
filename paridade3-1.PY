def main():
    num = int(input("Digite um número:"))
    if eh_par(num):
        print("é par")
    else:
        print("é impar")

def eh_par(num):
    return num % 2 ==0

main()