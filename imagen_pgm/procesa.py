import ImagenPGM as im

if __name__ == '__main__':
#   nombre = input('nombre de archivo: ')
    nombre = 'Lena_ascii'
    nombre = nombre + '.pgm'
    imagen1 = im.LeerImagen(nombre)
    im.EscribirImagen('duplica.pgm',imagen1)
    imagen2 = im.LeerImagen('duplica.pgm')    
    im.Informacion(imagen1)
    im.Informacion(imagen2)




