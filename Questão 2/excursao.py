print("=== EXCURSÃO DA ESCOLA ===")

while True:
	quantidade_turmas = input("Quantas turmas vão participar? ")
	if quantidade_turmas.isdigit() and int(quantidade_turmas) > 0:
		quantidade_turmas = int(quantidade_turmas)
		break
	print("Digite um número inteiro maior que zero.")

total_alunos = 0
maior_quantidade = -1
turma_mais_inscritos = ""

for numero in range(quantidade_turmas):
	print("Nome da turma", numero + 1)
	nome_turma = input()

	while True:
		print("Inscritos na turma", nome_turma)
		inscritos = input()
		if inscritos.isdigit():
			inscritos = int(inscritos)
			break
		print("Digite um número inteiro (0 ou mais).")

	total_alunos = total_alunos + inscritos

	if inscritos > maior_quantidade:
		maior_quantidade = inscritos
		turma_mais_inscritos = nome_turma

professores = (total_alunos + 14) // 15
total_pessoas = total_alunos + professores
onibus = (total_pessoas + 43) // 44
lugares_sobram = onibus * 44 - total_pessoas
custo_total = onibus * 1800

if total_alunos > 0:
	valor_por_aluno = custo_total / total_alunos
else:
	valor_por_aluno = 0

print("=== RESUMO ===")
print("Alunos:", total_alunos)
print("Professores acompanhantes:", professores)
print("Total de pessoas:", total_pessoas)
print("Ônibus necessários:", onibus, "(sobram", lugares_sobram, "lugares)")
print("Custo total: R$", custo_total)
print("Valor por aluno: R$", valor_por_aluno)
print("Turma com mais inscritos:", turma_mais_inscritos, "(", maior_quantidade, "alunos)")
