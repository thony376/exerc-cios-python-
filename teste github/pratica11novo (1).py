#desafio 1

nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))

media = (nota1 + nota2) /2

if media >=6: 
   print("Aprovado")

else:
   print("Reprovado")
    
#desafio 2

nota1 = float(input("Digite o primeiro numero"))
nota2 = float(input("Digite o segundo numero"))

if nota1 > nota2:
    print("{nota1} é o maior numero")
    print("{nota2} é o menor numero")
    
else:
    print("{nota2} é o maior numero")
    print("{nota2} é o menor numero")
    
#desafio 3

primeiranota = float(input("Digite a primeira nota"))
segundanota = float(input("Digite a segunda nota"))

media = (primeiranota+segundanota) /2

if media >= 7:
    print("Aprovado")
    
elif media <5:
    print("Recuperação")
    
else:
    print("Recuperação")
    
    
#desafio 4

nascimento = float(input("Digite seu ano de nascimento"))
anoAtual= 2024
idade = anoAtual-nascimento
idade2= datetime.now().years

if idade<=9:
    print("Sua categoria é mirim")

if (idade <=9 and idade <=14):
    print("Sua categoria é infantil")

if (idade>15 idade<=19):
     print("Sua categoria é JUNIOR")
     
     (idade>19 and idade<=24):
     print("Sua categoria é SENIOR")
    
if idade>25:
    print("Sua categoria é MASTER")

#desafio 5

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









#desafio 6
import random

op_jogador = int(input("Digite sua escolha: \n1-Pedra \n2-papel  \n3-Tesoura"))
# op_jogador = op_jogador.upper()

print(op_jogador)

if op_jogador ==1:
    tx_jogador="PEDRA"
if op_jogador ==2:
    tx_jogador="PAPEL"
if op_jogador ==3:
    tx_jogador="TESOURA"  
   
opcoes =["PEDRA","PAPEL","TESOURA"]
numero_randomico = random.randint(0,2)

print(opcoes)#random.randint(0,2)
print(opcoes[1])#PAPEL
 
op_computador= opcoes[numero_randomico]