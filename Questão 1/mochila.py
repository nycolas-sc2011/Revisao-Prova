limite = 15
nomes = []
pesos = []
peso_total = 0
quantidade = 0
item_mais_pesado = ""
peso_mais_pesado = 0

while True:
	nome = input("Nome do item (ou FIM para encerrar): ")

	if nome == "FIM" or nome == "fim":
		break

	while True:
		texto_peso = input("Peso em kg: ").replace(",", ".")
		if texto_peso.replace(".", "", 1).isdigit():
			peso = float(texto_peso)
			if peso > 0:
				break
		print("Peso inválido. Digite um número maior que zero.")

	nomes.append(nome)
	pesos.append(peso)
	quantidade = quantidade + 1
	peso_anterior = peso_total
	peso_total = peso_total + peso

	if peso > peso_mais_pesado:
		peso_mais_pesado = peso
		item_mais_pesado = nome

	if peso_anterior <= limite:
		if peso_total > limite:
			print("Atenção: o peso total passou de 15 kg!")

if quantidade == 0:
	print("A mochila está vazia.")
else:
	print("Itens na mochila:")
	indice = 0
	while indice < quantidade:
		print(indice + 1, nomes[indice], "-", pesos[indice], "kg")
		indice = indice + 1

	peso_medio = peso_total / quantidade

	print("Quantidade de itens:", quantidade)
	print("Peso total:", peso_total, "kg")
	print("Peso médio:", peso_medio, "kg")
	print("Item mais pesado:", item_mais_pesado, "-", peso_mais_pesado, "kg")

	if peso_total > limite:
		print("É preciso tirar", peso_total - limite, "kg da mochila.")
	else:
		print("Ainda cabem", limite - peso_total, "kg na mochila.")
