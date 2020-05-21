medida = float(input('Informe a medida em metros '))
print('{}m metros tem \n'
      '{}Km quilômetros\n'
      '{}hm hectômetro\n'
      '{}dm decâmetro\n'
      '{}dc decímetro\n'
      '{}cm centímetros e \n'
      '{}mm milímetros'
      .format(medida,
              medida/1000,
              medida/100,
              medida/10,
              medida*10,
              medida*100,
              medida*100
              ))
