from shared_function import abrir_archivo, separar, min_diferencia

def min_temp_spread(ruta):
    lineas= abrir_archivo(ruta)
    columnas= separar(lineas,3, 2)
    dif= min_diferencia(0,1,2, columnas)
    return dif

ruta= 'weather.dat'
minTemp= min_temp_spread(ruta)
print(minTemp)