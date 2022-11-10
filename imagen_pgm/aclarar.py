im = open('imagen/Lena_ascii.pgm')
magica = im.readline().rstrip('\n')

comentario = []
linea = im.readline().rstrip('\n')
while linea[0] == '#':
    comentario.append(linea)
    linea = im.readline().rstrip('\n')

tam = linea.split(' ')

ancho = int(tam[0])
alto = int(tam[2])

grises = int(im.readline().rstrip('\n'))
print(grises)
pixels = []

for linea in im:
    linea = linea.rstrip('\n')
    l = linea.split(' ')
    for pixel in l:
        if pixel != '':
            pixels.append(int(pixel))

binaria = []
for pixel in pixels:
    pixel = 255 - pixel 
    binaria.append(str(pixel))

sal = open('hoybinaria5.pgm','w')
sal.write('P2'+'\n')
sal.write('# Creada por Hugo Araya Carrasco \n')
sal.write(str(ancho)+' '+str(alto)+'\n')
sal.write('255\n')
for pixel in binaria:
    sal.write(str(pixel)+" ")
im.close()
sal.close()







