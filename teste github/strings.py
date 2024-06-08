texto= "Curso de Python"

print(texto)
print(texto [6]) #imprime a letra na ordem 6 (D)
print(texto [6:8]) 
print(texto[9:15]) #imprima python
print(texto[9:15:2]) #imprima (pto)

print(texto[:5]) #curso
print(texto[9:]) #python

print(len(texto)) #conta tamanho do string (15)
print(texto.count("o")) #quantas vezes aparece tal letra
print(f"letras 'o': {texto.count('o')}")

#procura em qual posição cada letra está
print(f"Existe Python?: {texto.find('Python')}") #9
print(f"Existe Python?: {texto.find('Python ')}") #-1 n encontrou
print(f"Existe Python?: {texto.find(' Python')}") #8

#indica a presença de uma palavra na frase
print(f"{'python' in texto}") #true
print(f"{' python' in texto}") #false

trocaTexto = texto.replace("python", "javascript")
print(trocaTexto)
print(texto)
print(f"Temos {texto} e {trocaTexto}, venha estudar com a gente")

textoMinusculo= texto.lower()
print(textoMinusculo)
textoMaisculo= texto.upper ()
print(textoMaisculo)

textoCapitalizado= texto.capitalize()
print(textoCapitalizado)
textoTitulo= texto.title()
print(textoTitulo)

texto2= " senai 1 "
textoSemEspaço=texto2.strip()
print(texto2)
print(textoSemEspaço)

juntaTexto= '-' .join(texto)
print(juntaTexto)
juntaTexto2 = ''.join(texto)
print(juntaTexto2)

divideTexto= texto.split()
print(divideTexto)
