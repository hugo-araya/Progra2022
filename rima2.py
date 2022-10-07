# Version 02
palabra1 = input('Palabra 1: ')
palabra2 = input('Palabra 2: ')
largo1 = len(palabra1)
largo2 = len(palabra2)
tres1 = palabra1[largo1-3:]
dos1 = palabra1[largo1-2:]
tres2 = palabra2[largo2-3:]
dos2 = palabra2[largo2-2:]
if tres1 == tres2:
    print('Riman')
else:
    if dos1 == dos2:
        print('Riman un poco')
    else:
        print('No riman')