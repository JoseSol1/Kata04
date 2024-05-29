def abrir_archivo(ruta):
    archivo=open(ruta, 'r')
    lineas=  archivo.readlines()
    return lineas
    
def separar(lineas, num_columnas, lineas_cabeza):
    datos=[]
    for linea in lineas[lineas_cabeza:]:
        columnas= linea.split()
        if len(columnas)<num_columnas:
            continue
        datos.append(columnas)
    return datos

def min_diferencia(col_inx1, col_inx2, col_inx3, datos):
    min_dif=100
    nombre_item= None
    for column in datos:
        try:
            nombre= column[col_inx1]
            valor1= int(column[col_inx2])
            valor2= int(column[col_inx3])
        except ValueError:
            continue
        dif= abs(valor1-valor2)
        if dif<min_dif:
            min_dif=dif
            nombre_item=nombre
    return nombre_item
