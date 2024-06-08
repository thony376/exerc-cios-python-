#desafio 1
numero1 = int(input("Digite um numero"))
numero2 = int(input("DIgite um numero"))
soma = numero1 + numero2
print("soma=", soma)

#desafio2
numeroInteiro = int(input("Digite um numero Inteiro"))
sucessor = numeroInteiro+ 1
antecessor = numeroInteiro- 1
print("numero sucessor=", sucessor)
print("numero antecessor=", antecessor)

#desafio3
num3= int(input("Digite um numero:"))
print(f"O dobro desse numero é {num3*2}, o triplo desse numero é {num3*3} o quadrado desse numero é {num3**2}")

#desafio4
nota1 = int(input("Digite a primeira nota do aluno"))
nota2 = int(input("Digite a segunda nota do aluno"))
print(f"A nota desses alunos é {nota1+nota2/2}")

#desafio5
dinheiro = int(input("Digite o dinheiro presente na carteira"))
print(f"Você possui {dinheiro/5}dolares")

#desafio extra1
numeroInteiro = int(input("Digite um numero inteiro"))
print(f"O quadrado desse numero e {numeroInteiro**2}")

#extra 2
caractere1 = int(input("caractere1"))
caractere2 = int(input("caractere2"))
print(f"O usuario digitou {caractere1} e {caractere2}")

#extra 4
base= int(input("Digite a base do retangulo"))
altura= int(input("Digite a altura do retangulo"))
print(f"A area do retangulo sera {base * altura}")
print(f"O perimetro do retangulo sera {base*2+altura*2}")

#extra 5
valor=float(input("Digite o valor da prestacao: "))
tempo=float(input("Digite o tempo de prestacao (em dias): "))
taxa=float(imput("Digite a taxa da prestacao: "))
prestacao = valor +(valor*(taxa/100) *tempo)
 
print(prestacao)