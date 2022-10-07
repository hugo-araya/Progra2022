# Version 01
palabra1 = input('Palabra 1: ')
palabra2 = input('Palabra 2: ')
tres1 = palabra1[-1] + palabra1[-2] + palabra1[-3]
dos1 = palabra1[-1] + palabra1[-2]
tres2 = palabra2[-1] + palabra2[-2] + palabra2[-3]
dos2 = palabra2[-1] + palabra2[-2]
if tres1 == tres2:
    print('Riman')
else:
    if dos1 == dos2:
        print('Riman un poco')
    else:
        print('No riman')
