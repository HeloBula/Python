#Operadores relacionais
A = 5
B  = 15
C = 20
print("A==B AND B<C:",A==B and B<C)
print("A+B == C:",A+B==C)
print("A<B OR B<C:",A<B or B<C)
print("NOT A==B: ",not A==B)

#Estrutura de decisão
X = input("Insira um valor para X:")
Y = input("Insira um valor para y:")

if (X>Y):
    aux = X
    X = Y
    Y = aux
    print("X agora é",X," e Y agora é",Y)
else:
    print("Y é maior que X")    
    
#Estrutura de repetição - for
print("\nContando de 1 a 10")
for n in range(1,11):
    print(n)
#For decrescente usa o Range com mais um parÂmetro
for t in range(10,0,-1):
    print(t)

#Estrutura de repetição - while
média = 0
soma = 0
qtd = 0
numero = float(input("Insira um valor para a média:"))

while (numero >0.0):
    soma = soma + numero
    qtd = qtd +1
    numero = float(input("Insira um valor para a média:"))
    
#Sai do loop, ou seja, numero < 0
print("Quantidade de números:",qtd)
print("Soma de valores:",soma)
print("Média:",soma/qtd)     