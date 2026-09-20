"""Exercício 3: Divisão de Cargas (Logística/Transporte): uma transportadora precisa levar 1.250
 caixas em caminhões pequenos.
 Cada caminhão suporta exatamente 12 caixas. Quantos caminhões sairão totalmente cheios? (Use //)
 e quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %)."""

carga_urgente = 1250
quantidade_caminhoes = carga_urgente // 12
quantos_caminhoes  = quantidade_caminhoes
sobra_caixas = carga_urgente % 12

print(f"A quantidade de caminhões que sairam totalmente cheios é: {quantos_caminhoes} ")
print(f"Sobraram {sobra_caixas} caixas para ir no caminhão menor")

