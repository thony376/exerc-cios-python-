#desafio1
def área(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno de {largura}m x {comprimento}m é de {area}m².')

# Exemplo de uso:
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
área(largura, comprimento)

#desafio2
def escreva(texto):
    tamanho = len(texto) + 4
    print('-' * tamanho)
    print(f'  {texto}  ')
    print('-' * tamanho)

escreva('Olá, mundo!!')
escreva('amo minha mulher!')

#desafio3
def maior(a, b, c):
    if a >= b and a >= c:
        maior_valor = a
    elif b >= a and b >= c:
        maior_valor = b
    else:
        maior_valor = c
    print(f'O maior valor entre {a}, {b} e {c} é {maior_valor}.')

#exemplo
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
maior(a, b, c)