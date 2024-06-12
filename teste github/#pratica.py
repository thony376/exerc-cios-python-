#desafio 1
nomeCompleto= input("Digite seu nome completo")")
print(f"Nome Maiusculo: {nomeCompleto.upper()}")
print(f"Nome Minusculo: {nomeCompleto.lower()}")

print(f"Seu Nome Completo possui: {len(nomeCompleto)} caracteres")
nomeCompletoSeEspaço = nomeCompleto.replace(" ", "")
print(f"Seu Nome Completo possui: {len(nomeCompletoSemEspaco)} letras")



#desafio 2
cidade=str(input("Qual o nome da sua cidade?"))
print(f"{'Santo' in cidade}")

#desafio 3
nome1=str(input("Qual o seu nome?"))
print(f"{'Silva' in nome1}"))

#desafio 4 
frase = input("Digite uma frase:" ).strip().lower()
QuantasVezesApareceA = frase.count('a')
primeiraPosicao = frase.find('a')
UltimaPosicao = frase.rfind('a') +1