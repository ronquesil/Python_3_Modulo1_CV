medida = float(input('Uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
#print('A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(n1, (n1/1000), (n1/100), (n1/10), (n1*10), (n1*100), (n1*1000)))
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
