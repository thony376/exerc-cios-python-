# # #EXERCÍCIO 1
# # # Faça um programa que leia duas notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média tem que ser no mínimo 6)
# nota1= float(input("Digite a primeira nota: "))
# nota2= float(input("Digite a segunda nota: "))

# if (nota1+nota2)/2>=6:
#     print("Aprovado!!!")
    
# else:
#     print("Reprovado")
    
# # #EXERCÍCIO 2
# # #Faça um programa que peça dois números ao usuário e mostre quem é o maior e quem é o menor:
# n1= float(input("Digite o primeiro número: "))
# n2= float(input("Digite o segundo numero: "))

# if n1>n2:
#     print(f"O {n1} é o maior número!")
#     print(f"O {n2} é o menor número!")
# else: 
#     print(f"O {n2} é o maior número!")
#     print(f"O {n1} é o menor número!")
    
# # #EXERCÍCIO 3
# #Escreva um programa que diga se o número escolhido pelo usuário é par ou ímpar:
# n3= float(input("Escolha um número:"))

    
# # #EXERCÍCIOS: CONDIÇÕES ANINHADAS

# # #DESAFIO 01
# # #Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# # # # Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# valorCasa= float(input("Digite o valor da casa: "))
# salario= float(input("Qual é o valor do seu salário? "))
# anosPagando= float(input("Em quantos anos você pretende pagar? "))

# meses=anosPagando*12
# prestação=valorCasa/meses
# print(f"Meses a pagar= {meses}")
# print(f"Valor da prestação= {prestação}")
# porcentagem= salario*0.3

# if prestação>porcentagem:
#     print("Compra negada")
# else:
#     print("Compra Permitida")

# # # #DESAFIO 02
# # # #Escreva um programa que leia dois números inteiros e compare- os, mostrando na tela uma mensagem:
# # # # O primeiro valor é maior
# # # # O segundo valor é maior
# # # # Não existe valor maior, os dois são iguais
# primeiroNumero= float(input("Escolha o primeiro numero: "))
# secundoNumero= float(input("Escolha o segundo numero: "))

# if primeiroNumero>secundoNumero:
#     print(f"O {primeiroNumero} é o maior e o {secundoNumero} é o menor")

# if secundoNumero>primeiroNumero:
#     print(f"O {primeiroNumero} é o menor e o {secundoNumero} é o maior")
    
# if secundoNumero==primeiroNumero:
#     print("Os dois números são iguais")
    
# #DESAFIO 03
# # Crie um programa que leia duas notas entre 0 a 10 de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# # Média abaixo de 5.0: REPROVADO
# # Média entre 5.0 a 6.9: RECUPERAÇÃO
# # Média igual ou superior a 7.0: APROVADO
# primeiranota= float(input("Digite a primeira nota: "))
# segundanota= float(input("Digite a seguna nota:"))
# media= (primeiranota+segundanota)/2

# if media >= 7:
#     print("Aprovado!")
# elif media < 5:
#     print("Reprovado")
# else:
#     print("Recuperação")
    
# #DESAFIO 04
# #A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.
# # Até 9 anos: MIRIM
# # Até 14 anos: INFANTIL
# # Até 19 anos: JUNIOR
# # Até 24 anos: SÊNIOR
# # Acima: MASTER
# nascimento= float(input("Digite seu ano de nascimento: "))
# anoAtual=2024
# idade= anoAtual-nascimento
# # idade2= datetime.now().years
# if idade<=9:
#     print("Sua categoria é a MIRIM")

# if (idade>9 and idade<=14):
#     print("Sua categoria é a INFANTIL")

# if (idade>15 and idade<=19):
#     print("Sua categoria é JUNIOR")

# if (idade>19 and idade<=24):
#     print("Sua categoria é SENIOR")
    
# if idade>25:
#     print("Sua categoria é MASTER")
    
    
#DESAFIO 05
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferente
a= float(input("Digite o valor da primeira reta: "))
b= float(input("Digite o valor da segunda reta reta: "))
c= float(input("Digite o valor da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print("Será possível formar um triângulo!") 
    if a==b==c:
        print("Esse triângulo é um triângulo equilátero")
    if a==b or a==c or b==c:
        print("Esse triângulo é um triângulo isóceles")
    if a!=b or a!=c or b!=c:
        print("Esse triângulo é escaleno")
else:
    print("Não é possível formar um triângulo")
