print('Matematica')
examen_mat = float(input('Examen: '))
tarea_mat_1 = float(input('Tarea 1: '))
tarea_mat_2 = float(input('Tarea 2: '))
tarea_mat_3 = float(input('Tarea 3: '))
tareas_mat = (tarea_mat_1+tarea_mat_2+tarea_mat_3)/3
promedio_mat = examen_mat*0.9 + tareas_mat*0.1
print()
print('Fisica')
examen_fis = float(input('Examen: '))
tarea_fis_1 = float(input('Tarea 1: '))
tarea_fis_2 = float(input('Tarea 2: '))
tareas_fis = (tarea_fis_1+tarea_fis_2)/2
promedio_fis = examen_fis*0.8 + tareas_fis*0.2
print()
print('Programacion')
examen_pro = float(input('Examen: '))
tarea_pro_1 = float(input('Tarea 1: '))
tarea_pro_2 = float(input('Tarea 2: '))
tarea_pro_3 = float(input('Tarea 3: '))
tareas_pro = (tarea_pro_1+tarea_pro_2+tarea_pro_3)/3
promedio_pro = examen_pro*0.85 + tareas_pro*0.15
promedio_final = (promedio_mat+promedio_fis+promedio_pro)/3
print()
print('Promedio mtematica: ', promedio_mat)
print('Promedio fisica: ', promedio_fis)
print('Promedio programacion: ', promedio_pro)
print('Promedio final: ', promedio_final)
