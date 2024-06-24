#desafio 1

numero1= int(input("Digite o primeiro numero"))
numero2= int(input("Digite o segundo numero"))
numero3= int(input("Digite terceiro numero"))
numero4= int(input("Digite o quarto numero"))
numero5= int(input("Digite o quinto numero"))

lista = [1, 2, 3, 4, 5]
print(lista)

lista.sort()
print(lista)
menorNumero.append(1)


#versão 2

numero = []
maior = menor = 0

for i in range(0,5):
    numero= int(input(f"Digite o {i+1} numero: "))
    numeros.append(numero)
    
    if i==0:
        maior = menor = numero
    else:
        if numero > maior:
            maior= numero
            if numero < menor:
                menor = numero
                
print("Numeros inseridos: ")
print(numero)
print(" ")
print(f"Menor numero = {menor}")
print(f"Maior numero {maior}")



#desafio 2

valor = []

while True:
    numero = int(input("Digite um numero entre 0 e 100: (Digite -1 se quiser sair) "))
    print(" ")
    
    if numero in valor:
        print("Numero ja cadastrado. Tente outro")
    else:
         valor.append(numero)
         print(valor)
        
    if numero == -1:
        print(" ")
        print("Saindo...")
        break
print(" ")
print("---------------")
print("Lista completa")
print(valor)
print("ordem crescente:")
valor.sort()
print(valor)
    







#desafio 3
lista = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    
    if i == 0:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1
        else:
            lista.append(valor)

print("Lista ordenada:", lista)



#desafio 4

numeros = []
pares = []
impares = []

while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Todos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
     
    
    
    
    
#desafio 5
pessoas = []
mais_pesado = mais_leve = 0

while True:
    nome = input("Nome da pessoa (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    peso = float(input("Peso da pessoa: "))
    pessoas.append((nome, peso))
    
   
    if peso > mais_pesado:
        mais_pesado = peso
    if mais_leve == 0 or peso < mais_leve:
        mais_leve = peso

qtd_pessoas = len(pessoas)

pessoas_pesadas = [pessoa[0] for pessoa in pessoas if pessoa[1] == mais_pesado]

pessoas_leves = [pessoa[0] for pessoa in pessoas if pessoa[1] == mais_leve]

print(f"A) Quantidade de pessoas cadastradas: {qtd_pessoas}")
print("B) Pessoas mais pesadas:")
for pessoa in pessoas_pesadas:
    print(f"   - {pessoa}")
print("C) Pessoas mais leves:")
for pessoa in pessoas_leves:
    print(f"   - {pessoa}")



#desafio 6

valores = [[], []]


for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        valores[0].append(valor)  #Par
    else:
        valores[1].append(valor)  #Ímpar


valores[0].sort()
valores[1].sort()

print("Valores pares:", valores[0])
print("Valores ímpares:", valores[1])





#desafio 7

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}", end=" ")  
    print() 








#desafio 8

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}", end=" ")
    print()  

soma_pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            soma_pares += valor

soma_terceira_coluna = 0
for linha in matriz:
    soma_terceira_coluna += linha[2]

maior_segunda_linha = max(matriz[1])


print(f"\nA) Soma dos valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")










    
