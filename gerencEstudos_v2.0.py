import os


def check(x):
    a = 0
    for y in x:
        a = y + a
    return int(a)


def imprimeVal(x):
    for y in x:
        print("\t", y, end="")
    print("")


def calculaHoras(fat, horas):
    aux = 0
    for x in range(len(fat)):
        aux = aux + fat[x] * horas[x]
    return aux


def addReg(x):
    x.append(input())
    x.pop(0)
    return x

def gravaLista(lista,arqv):
    texto = ""
    for x in lista:
        texto += str(x) + "\t"
    arqv.write(texto+"\n")


fatores = [0.06, 0.08, 0.08, 0.09, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14]
datas = ["07/11", "08/11", "09/11", "10/11", "11/11", "12/11", "13/11", "14/11", "15/11", "16/11"]
horas = [3.41, 3, 0.2, 3.95, 4.06, 2.02, 1.74, 2.63, 4.31, 5.71]
'''
while True:
    os.system('cls')
    print("\t\tESCOLHA A OPÇÃO\n")
    print("1 - Checar valores ")
    print("2 - Adicionar nova data")
    print("3 - Calcular as novas horas ")
    print("4 - Sair")
    op = int(input("\nSua opção: "))

    if op == 1:
        print("Dias: ", end="\t")
        imprimeVal(datas)
        print("Horas: ", end="\t")
        imprimeVal(horas)
        print("Fatores: ", end="")
        imprimeVal(fatores)
        print("Soma dos fatores: ", check(fatores))
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
'''
'''
arq = open('PÁGINAS PENDENTES.txt')
count = 0
for x in arq:
    count += 1
    print(x)
print(count)
'''
arqv = open("dados.txt",'r')


arqv.close()
arqv = open("dados.txt",'w')
gravaLista(fatores,arqv)
gravaLista(datas,arqv)
gravaLista(horas,arqv)
arqv.close()