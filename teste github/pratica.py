#desafio 1
nomeCompleto= input("Digite seu nome completo")
print(f"Nome Maiusculo: {nomeCompleto.upper()}")
print(f"Nome Minusculo: {nomeCompleto.lower()}")

print(f"Seu Nome Completo possui: {len(nomeCompleto)} caracteres")
nomeCompletoSeEspaço = nomeCompleto.replace(" ", "")
print(f"Seu Nome Completo possui: {len(NomeCompletoSemEspaco)} letras")


#desafio 2
cidade=str(input("Qual o nome da sua cidade?"))
divideNomeCidade = nomeCidade.split()
primeiroNomeCidade = divideNomeCidade[0].upper()
verificaPalavraEmFrase = "SANTO" in primeiroNomeCidade
print(f"O nome da cidade {divideNomeCidade} começa com Santo: {verificaPalavraEmfrase}")

#desafio 3
nome1=str(input("Qual o seu nome?"))
print(f"{'Silva' in nome1}")

#desafio 4 
frase = input("Digite uma frase:" ).strip()
QuantasVezesApareceA = frase.count('a')
primeiraPosicao = frase.find('a')
UltimaPosicao = frase.find('a ')

#desafio 5
nomeCompleto= str(input("Digite seu nome completo)"))
divideNome = nomeCompleto.split() #Inicia cada palavra dentro de um array
tamanhoArray = len(divideNome)
inicioNome = divideNome[0]
fimNome = divideNome[tamanhoArray - 1]

print(f"Primeiro Nome: {inicioNome}")
print(f"Ultimo Nome: {fimNome}")