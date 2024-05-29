from shared_function import abrir_archivo, separar, min_diferencia

def min_goal_dif(ruta):
    lineas= abrir_archivo(ruta)
    columnas= separar(lineas,9, 1)
    dif= min_diferencia(1,6,8, columnas)
    return dif

ruta= 'football.dat'
minTemp= min_goal_dif(ruta)
print(minTemp)