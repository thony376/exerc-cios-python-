#desafio1
aluno = {}

aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Média do aluno: '))

if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print('\n--- Dados do Aluno ---')
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
    
    
    
 #desafio2
 import random

resultados = {}

for jogador in range(1, 5):
    resultados[f'Jogador {jogador}'] = random.randint(1, 6)

print('--- Resultados dos Jogadores ---')
for jogador, resultado in resultados.items():
    print(f'{jogador}: {resultado}')

vencedor = max(resultados, key=resultados.get)
print(f'\nVencedor: {vencedor} com {resultados[vencedor]} pontos.')



#desafio3
from datetime import date

pessoa = {}

pessoa['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - ano_nascimento
pessoa['ctps'] = int(input('Número da CTPS (0 se não tiver): '))

if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['ano_contratacao'] + 35 - ano_nascimento

print('\n--- Dados da Pessoa ---')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
    
    
    
#desafio4
jogador = {}

jogador['nome'] = input('Nome do jogador: ')
num_partidas = int(input('Quantidade de partidas jogadas: '))

jogos = []
total_gols = 0
for partida in range(1, num_partidas + 1):
    gols = int(input(f'Gols na partida {partida}: '))
    jogos.append(gols)
    total_gols += gols

jogador['gols'] = jogos
jogador['total_gols'] = total_gols

print('\n--- Aproveitamento do Jogador ---')
for chave, valor in jogador.items():
    print(f'{chave}: {valor}')
    
    
#desafio5
pessoas = []
soma_idades = 0
mulheres = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo (M/F): ').upper()
    pessoa['idade'] = int(input('Idade: '))
    soma_idades += pessoa['idade']
    
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    
    pessoas.append(pessoa)
    
    continuar = input('Deseja continuar cadastrando? (S/N) ').upper()
    if continuar != 'S':
        break

num_pessoas = len(pessoas)
media_idades = soma_idades / num_pessoas if num_pessoas > 0 else 0

print(f'\nA) Total de pessoas cadastradas: {num_pessoas}')
print(f'B) Média de idade do grupo: {