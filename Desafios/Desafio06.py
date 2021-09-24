n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2) # a raiz quadrada de um número é ele elevada a potência de 1/2
#print('O dobro de {} vale {}, o triplo é {} e a raiz quadrada é {}'.format(n, d, t, r)) #print em uma linha e usando 4 variáveis)
print('O dobro de {} vale {}. \nO triplo vale {}. \nA raiz quadrada é igual a {:.2f}'.format(n, (n * 2), (n * 3), (n ** (1/2)))) #usando uma variável e dividido em linhas
