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






#desafio 4

while True:
    num = int(input("Digite um numero (0 para sair): "))
    
    par = numero %2==0
    impar = numero %2==1 
    
     
    
    
    
    
#desafio 5






#desafio 6






#desafio 7








#desafio 8
    

