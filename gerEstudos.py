import os

def check(x):
    a = 0
    for y in x:
        a = y + a
    return int(a)

def imprimeVal(x):
    for y in x:
        print("\t",y,end="")
    print("")

def calculaHoras(fat,horas):
    aux = 0
    for x in range(len(fat)):
        aux = aux + fat[x]*horas[x]
    return aux

def addReg(x):
    x.append(input())
    x.pop(0)
    return x

fatores = [0.06,0.08,0.08,0.09,0.09,0.1,0.11,0.12,0.13,0.14]
datas = ["20/out","21/10","22/10","23/10","24/10","25/10","26/10","27/10","28/10","29/10"]
horas = [4.00,5.57,4.14,5.4,7.27,5.06,4.27,5.71,3.26,0.25]


while True:
    os.system('cls')
    print("\t\tESCOLHA A OPÇÃO\n")
    print("1 - Checar valores ")
    print("2 - Adicionar nova data")
    print("3 - Calcular as novas horas ")
    print("4 - Sair")
    op = int(input("\nSua opção: "))

    if op == 1:
        print("Dias: ",end="\t")
        imprimeVal(datas)
        print("Horas: ",end="\t")
        imprimeVal(horas)
        print("Fatores: ",end="")
        imprimeVal(fatores)
        print("Soma dos fatores: ",check(fatores))
    elif op == 2:
        print("Digite a nova data: ", end="")
        datas = addReg(datas)
        print("Digite as horas desse dia: ", end="")
        horas = addReg(horas)
        horas[9] = float(horas[9])
    elif op == 3:
        print(round(calculaHoras(fatores, horas), 2))
    elif op == 4:
        break