#Primeiro código em Python
print("Hello World")

codigo = 10
salario = 1500.00
situacao = True

tipo = type(salario)

print(salario)
print(tipo)

nome = input("Digite o nome: ")

print('Nome dela é',nome,'e o salário inicial é', salario)

fruta = input("Qual a fruta favorita: ")
print(fruta)
print("Código:", codigo)


#Funções
def coletaNumero():
    n = float(input("Digite uma nota:"))
    return n


def mediaNota(n1,n2):
    print("Nota 1:",n1)
    print("Nota 2:",n2)
    média=float((n1+n2)/2)
    print("Média:",média,"\nSituação:")
    if(média>=7):
          print("Aprovado")
    else:
        print("Reprovado")   

a = coletaNumero()
b = coletaNumero()
mediaNota(a,b)