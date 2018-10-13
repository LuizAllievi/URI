codigo, quantidade = map(int, input().split())

valores = [4.00, 4.50, 5.00, 2.00, 1.50]

total = valores[codigo - 1] * quantidade

print("Total: R$ {:.2f}".format(total))
