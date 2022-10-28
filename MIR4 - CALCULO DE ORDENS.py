def calcula_imposto(price):
    if price < 20:
        return 1
    else:
        return (price*0.05)//1

qtdp = int(input("Informe a qtd possuída do produto: "))
qtdm = int(input("Informe a qtd de produtos da 1ª ordem do livro: "))
priceM = int(input("Informe o preço da 1ª ordem do livro: "))

unit_price = priceM/qtdm
qtd39G = (39/unit_price)//1+1

qtd_list = []
spreads = []
price_ord = []
price_liq = []


for x in range(qtdp,0,-1):
#    print(x)
    if x >= qtd39G:
        qtd_list.append(qtd39G)
        priceOrd = 39
        price_liq.append(priceOrd-1)
        spreads.append(round((unit_price-qtd39G/priceOrd)*x,2))
        break
    elif (x*unit_price)//1 < 10:
        break
    else:
        qtd_list.append(x)
        priceOrd = x*unit_price//1
        spreads.append(round((unit_price - (priceOrd/x))*x,2))
        price_liq.append(int(priceOrd - calcula_imposto(priceOrd)))




'''
print("Ordem de 39 gold: ", qtd39G)
print("\nQuantidade a ser registrada: ", qtd_list)
print("Preço de registro: ", price_liq)
print("Spreads: ", spreads)
'''
print(qtd_list)
print("Quantidade\tSpread\t\tLucro líquido")
for y in range(len(qtd_list)):
    print(qtd_list[y],"\t\t",spreads[y],"\t\t",price_liq[y])


input("")

