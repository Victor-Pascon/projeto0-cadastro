print(f'{" Desafio 010 - Converção Monetaria ":=^90}')

# Pergunta ao Usuario
Reais = float(input('Quantos Reais deseja trocar por outras moedas? R$'))

# Resposta ao Usuario
print('Com R${:.2f} podemos comprar as seguintes quantidades de moedas estrangeiras'.format(Reais))
print(f'{"":_>90}')
print('Dolares Americanos: ${:.2f}'.format(Reais * 0.21))
print('Iene Japonês: ¥{:.2f}'.format(Reais * 27.08))
print('Euro: €{:.2f}'.format(Reais * 0.19))
print(f'{"":_>90}')
