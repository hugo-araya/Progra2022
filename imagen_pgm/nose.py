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

pixels = []

for linea in im:
    linea = linea.rstrip('\n')
    l = linea.split(' ')
    for pixel in l:
        if pixel != '':
            pixels.append(int(pixel))

binaria = []
i = 0
print((len(pixels)))
while i < len(pixels):
    if (i % 2) == 0:
        binaria.append(str(pixels[i]))
    i = i + 1
print(len(binaria))
sal = open('imagen/binaria6.pgm','w')
sal.write('P2'+'\n')
sal.write('# Creada por Hugo Araya Carrasco \n')
sal.write(str(int(ancho/2))+' '+str(int(alto/2))+'\n')
sal.write('255\n')
for pixel in binaria:
    sal.write(str(pixel)+" ")
im.close()
sal.close()







