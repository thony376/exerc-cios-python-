#desafio 1

import random

print("Jogo do numero")
numeroUsuario= int(input("Digite um numero entre 0 e 5: "))

numeroComputador = random.randint(0,5)
print(f"Numero escolhido PC: {numeroComputador}")

if numeroUsuario==numeroComputador:
       print("Parabens, voce venceu a maquina :) ")
else:
       print("Que bosta, voce perdeu otario")
       


#desafio 2
velocidade = float(input("Digite a velocidade do carro (Km/h): "))


if velocidade>80:
   print("sofreu multa")
   acima_do_limite= velocidade-80
   print(f"Km acima do limite permitido: {acima_do_limite} km/h")
   multa= acima_do_limite*7
   print(f"Multa = R${multa} ")


#desafio 3
distanciaDaViagem = float(input("Diga a distancia da viagem em (Km): "))

if distanciaDaViagem<=200:
    passagem= distanciaDaViagem*0.50
    print(f"o preco da sua passagem é {passagem} R$")

else:
      passagem = distanciaDaViagem*0.45
      print(f"o preco da sua passagem é {passagem} R$")


#desafio 4
numero1 = float(input("Digite o primeiro numero"))
numero2 = float(input("Digite o segundo numero"))
numero3 = float(input("Digite o terceiro numero"))

#desafio 5
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")