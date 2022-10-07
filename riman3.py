# Version 03
palabra1 = input('Palabra 1: ')
palabra2 = input('Palabra 2: ')
if palabra1[len(palabra1)-3:] == palabra2[len(palabra2)-3:]:
    print('Riman')
else:
    if palabra1[len(palabra1)-2:] == palabra2[len(palabra2)-2:]:
        print('Riman un poco')
    else:
        print('No riman')