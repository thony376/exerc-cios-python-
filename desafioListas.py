desafio 1

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
valores = []

for i in range(5):
    num = int(input("Digite um valor numérico: "))
    if i == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1

print("Lista ordenada:", valores)







#desafio 4

while True:
    num = int(input("Digite um numero (0 para sair): "))
    
    par = numero %2==0
    impar = numero %2==1 
    
     
    
    
    
    
#desafio 5
pessoas = []

while True:
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa: "))
    pessoas.append([nome, peso])
    
    cont = input("Quer continuar? (S/N): ").strip().upper()
    if cont == 'N':
        break

quantidade = len(pessoas)
pesos = [p[1] for p in pessoas]
max_peso = max(pesos)
min_peso = min(pesos)

mais_pesados = [p[0] for p in pessoas if p[1] == max_peso]
mais_leves = [p[0] for p in pessoas if p[1] == min_peso]

print(f"A) Quantidade de pessoas cadastradas: {quantidade}")
print(f"B) Pessoas mais pesadas ({max_peso} kg): {mais_pesados}")
print(f"C) Pessoas mais leves ({min_peso} kg): {mais_leves}")





#desafio 6
numeros = [[], []]

for i in range(7):
    num = int(input("Digite um valor numérico: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print("Valores pares em ordem crescente:", numeros[0])
print("Valores ímpares em ordem crescente:", numeros[1])





#desafio 7
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor para a posição ({i},{j}): "))
        linha.append(valor)
    matriz.append(linha)

# Exibição da matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:4}", end='')  # Formatação para espaçamento uniforme
    print()








#desafio 8
# Criação de uma matriz 3x3 e preenchimento com valores lidos do teclado
matriz = []
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor para a posição ({i},{j}): "))
        linha.append(valor)

        # Verifica se o valor é par e soma
        if valor % 2 == 0:
            soma_pares += valor

        # Soma dos valores da terceira coluna
        if j == 2:
            soma_terceira_coluna += valor

        # Maior valor da segunda linha
        if i == 1:
            if j == 0 or valor > maior_segunda_linha:
                maior_segunda_linha = valor

    matriz.append(linha)

# Exibição da matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:4}", end='')
    print()

# Resultados adicionais
print(f"\nA) Soma de todos os valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")



































