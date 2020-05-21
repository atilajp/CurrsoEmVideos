larg = float(input('Informe a Largura da parede: '))
alt = float(input('Informe a altura da parede: '))
parede = larg * alt
print('Sua parede tem {:.2f}m2'.format(parede))
print('Ira consumir {:.4f} litros de tinta'.format(parede/2))

