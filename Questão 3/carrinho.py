def subtotal_item(preco, quantidade=1):
	return preco * quantidade


def aplicar_cupom(total, cupom):
	cupom = cupom.strip().upper()
	percentual = 0

	if cupom == "PROMO10":
		percentual = 10
	elif cupom == "VOLTAASAULAS":
		percentual = 15
	elif cupom == "BLACK25":
		percentual = 25

	novo_total = total - total * percentual / 100
	return novo_total, percentual


def calcular_frete(total, gratis_acima=200.0, valor=25.0):
	if total >= gratis_acima:
		return 0.0
	return valor


def valor_parcela(total, parcelas=1):
	if parcelas <= 6:
		return total / parcelas
	return total * (1 + 0.02 * parcelas) / parcelas


print("=== LOJA VIRTUAL ===")
subtotal = 0

while True:
	produto = input("Produto (Enter para fechar o carrinho): ").strip()
	if produto == "":
		break

	while True:
		texto_preco = input("Preço (R$): ").strip().replace(",", ".")
		if texto_preco.replace(".", "", 1).isdigit():
			preco = float(texto_preco)
			if preco > 0:
				break
		print("Digite um valor maior que zero.")

	while True:
		texto_quantidade = input("Quantidade: ").strip()
		if texto_quantidade.isdigit() and int(texto_quantidade) > 0:
			quantidade = int(texto_quantidade)
			break
		print("Digite um número inteiro maior que zero.")

	valor_item = subtotal_item(preco, quantidade)
	subtotal = subtotal + valor_item
	print(" " + str(quantidade) + " x " + produto + " = R$ " + format(valor_item, ".2f") + " (carrinho: R$ " + format(subtotal, ".2f") + ")")

cupom = input("Cupom de desconto (Enter se não tiver): ")
total_com_desconto, percentual = aplicar_cupom(subtotal, cupom)

if percentual == 0 and cupom.strip() != "":
	print("Cupom inválido.")

desconto = subtotal - total_com_desconto
frete = calcular_frete(total_com_desconto)
total = total_com_desconto + frete

while True:
	texto_parcelas = input("Em quantas parcelas (1 a 12)? ").strip()
	if texto_parcelas.isdigit() and int(texto_parcelas) >= 1 and int(texto_parcelas) <= 12:
		parcelas = int(texto_parcelas)
		break
	print("Digite um número de 1 a 12.")

parcela = valor_parcela(total, parcelas)

print("=== NOTA ===")
print("Subtotal: R$ " + format(subtotal, ".2f"))
print("Desconto:", percentual, "% (R$ " + format(desconto, ".2f") + ")")
print("Frete: R$ " + format(frete, ".2f"))
print("Total: R$ " + format(total, ".2f"))
print("Pagamento:", parcelas, "x R$ " + format(parcela, ".2f"))
