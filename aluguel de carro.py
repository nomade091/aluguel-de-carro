# Constantes
TAXA_DIARIA = 60
TAXA_KM = 0.15

# Entrada do usuário
dias = int(input('Quantos dias alugado: '))
km = float(input('Quantos km rodados: '))

# Cálculo do valor a pagar
valor_a_pagar = (dias * TAXA_DIARIA) + (km * TAXA_KM)

# Saída formatada
print(f'O total a pagar é de R${valor_a_pagar:.2f}')
