"""Exercício 2: Controle de Estoque de E-commerce (Logística):
um e-commerce começou o dia com 250 unidades de um smartphone no estoque.
Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um fornecedor.
Atualize a variável de estoque e exiba o saldo final."""

inicial_estoque = 250
vendidos = 78
chegada = 100

saldo_final = (inicial_estoque - vendidos) + chegada

print(f"Saldo final: {saldo_final}")