path = r"D:\Python\primeros_proyectos\mat.txt"
archivo = open(path,"rt")

matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for line in archivo:
    line = line.split()
    print(line)

"""
N, M = map(int, archivo.readline().rstrip())

for i in range(1,N):
    for j in range(1,M):
        matriz[i,j]=int(archivo.read())

print(matriz)
"""

archivo.close()
