import os


def piso(x):
    if x // 1 == x:
        return (x // 1) - 1
    else:
        return x // 1


def otimizaOrdem():
    os.system("cls")
    nPossuido = int(input("Produtos possuídos: "))
    nLivro = int(input("Nº de produtos do livro: "))
    priceLivro = int(input("Preço da ordem do livro: "))

    priceUnit = priceLivro / nLivro
    n39 = int((39 * priceUnit ** (-1)) // 1 + 1)

    print("\nPreço unitário do mercado: {:.5}".format(priceUnit))
    print("Nº de produtos para uma ordem de 39 de gold: ", n39)

    if nPossuido >= n39:
        print("\n\n\t\t______________\n\t\tORDEM DE VENDA")
        print("Nº de produtos: 39")
        print("Valor de ordem:", n39, "\n\n\n\n")
    else:
        aux = piso(nPossuido * priceUnit)
        print("\n\nOrdens tentadas:")
        for x in range(nPossuido, 0, -1):
            print("\t", x + 1, "a", round((x + 1) * priceUnit, 2), "de gold")
            if x * priceUnit < 10:
                print("Quantidade insuficiente para registrar ordens, a ordem mínima é de 10 de gold")
                break
            if aux != piso(x * priceUnit):
                print("\t", x, "a", round(x * priceUnit, 2), "de gold")
                print("\n\n\t\tORDEM DE VENDA")
                print("Nº de produtos:", x + 1)
                print("Valor de ordem:", int(aux))
                break


while True:
    otimizaOrdem()
    b = input("\n\n\n\nDeseja parar de registrar ordens? ")
    if b == "Sim" or b == "Yes" or b == "S" or b == "Y" or b == "y" or b == "s":
        break
