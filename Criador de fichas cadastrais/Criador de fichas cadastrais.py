numalunos = int(input('Quantos novos alunos vão abrir fichas de cadastro? '))

for c in range(1, numalunos+1):
    nome = str(input(f'Nome do aluno {c}: '))
    idade = int(input(f'Idade de {nome}: '))
    texto = open(f'Aluno {nome}.txt', 'wt')
    texto.write(f'Nome: {nome}\n')
    texto.write((f'Idade: {idade}'))
    texto.close()

