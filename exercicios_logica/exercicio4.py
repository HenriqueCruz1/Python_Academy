"""Exercício 4: Análise de Margem de Lucro (Financeiro): uma consultoria faturou R$ 15.000,00 em um projeto.
Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%. 
Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento). 
No final, crie uma variável booleana chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%)."""

custos_fixos = 50000
faturamento = 15000 - custos_fixos
imposto_faturamento = ((faturamento/100)*15)*faturamento
lucro_liquido = faturamento - imposto_faturamento
margem_lucro = (lucro_liquido/faturamento)/100 

print(f"Faturamento: {faturamento}")
print(f"Imposto: {imposto_faturamento}")
print(f'Lucro: {lucro_liquido}')
print(f"Margem de lucro: {margem_lucro}")

while True:
    if margem_lucro > 0.30:
        print("Meta atingida")
        break
    else:
        print("Meta não atingida")
        break



