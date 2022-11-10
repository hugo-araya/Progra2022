def Configuracion(clave):
    config = {
        'autor': '# << Hugo Araya Carrasco - 2022 >>'
    }
    return config[clave]

def CreaImagen():
    imagen = {
        'magica': 'XX', 
        'comentario': [],
        'ancho': 0,
        'alto': 0,
        'gris': 0,
        'pixeles': []
    }
    return imagen

def LeerImagen(nombre):
    im = open('Image/'+nombre)
    magica = im.readline().rstrip('\n')
    comentario = []
    linea = im.readline().rstrip('\n')
    while linea[0] == '#':
        comentario.append(linea)
        linea = im.readline().rstrip('\n')
    sep = ' '
    dimension = linea.split(sep)
    ancho = int(dimension[0])
    if len(dimension[1]) == 0:
        alto = int(dimension[2])
    else:
        alto = int(dimension[1])
    grises = int(im.readline().rstrip('\n'))
    pixeles = []
    for linea in im:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        for pixel in lista:
            if pixel != '':
                pixeles.append(int(pixel)) 
    imagen = CreaImagen()
    imagen['magica'] = magica
    imagen['comentario'] = comentario[:]
    imagen['ancho'] = ancho
    imagen['alto'] = alto
    imagen['gris'] = grises
    imagen['pixeles'] = pixeles[:]
    im.close()
    return imagen

def Magica(imagen):
    return imagen['magica']

def Comentario(imagen):
    return imagen['comentario']

def Ancho(imagen):
    return imagen['ancho']

def Alto(imagen):
    return imagen['alto']

def Grises(imagen):
    return imagen['gris']

def Informacion(imagen):
    print('Tipo:', Magica(imagen))
    comen = Comentario(imagen)
    if len(comen) == 0:
        print('Imagen sin comentarios')
    else:
        print('Comentarios')
        for c in comen:
            print(' ', c)
    print('Ancho :', Ancho(imagen))
    print('Alto  :', Alto(imagen))
    print('Grises:', Grises(imagen))
    print('Promedio: ', PromedioPixeles(imagen))

def Pixeles(imagen):
    return imagen['pixeles']

def PromedioPixeles(imagen):
    total = Ancho(imagen) * Alto(imagen)
    suma = 0
    pixeles = Pixeles(imagen)
    suma = sum(pixeles)
    return  suma / total

def EscribirImagen(nuevoNombre, imagen):
    sal = open('Image/'+nuevoNombre,'w')
    sal.write(Magica(imagen)+'\n')
    comen = Comentario(imagen)
    if len(comen) !=0:
        ok = False
        for c in comen:
            if c == Configuracion('autor'):
                ok = True
            sal.write(c+'\n')
        if ok != True:
            sal.write(Configuracion('autor')+'\n')
    sal.write(str(Ancho(imagen))+' '+str(Alto(imagen))+'\n')
    sal.write(str(Grises(imagen))+'\n')
    nueva = Pixeles(imagen)
    for pixel in nueva:
        sal.write(str(pixel)+' ')
    sal.write('\n')
    sal.close()

