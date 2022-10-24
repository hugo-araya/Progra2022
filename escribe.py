sal = open('seba.txt','w')
i = 0
while i < 3:
    palabra = input('Palabra: ')
    sal.write(palabra+'\n')
    i = i + 1
sal.close()
