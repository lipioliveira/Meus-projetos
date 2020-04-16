#conversor de medidas
#(km, hm, dam, m, cm, mm)

medida = float(input('Insira a medida em metros para ver a conversão:'))
print('A medida de {:.2f} metros representa {:.3f} em km, {:.2f} em hm, {:.1f} em dam, {:.0f} dm, {:.0f}cm e {:.0f}mm'.format(medida , (medida/1000), (medida/100), (medida/10), (medida*10), (medida*100), (medida*1000))) 