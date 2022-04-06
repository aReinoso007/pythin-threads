import multiprocessing
import numpy as np
import sys
from multiprocessing import Process
import time 

#N = int( sys.argv[1])
N = int(10000)
Pros = 3
A = np.random.randint(60, size=N) #para guardar el resultado
B = np.random.randint(60, size=(N,N)) #la matriz con la que se debe multiplicar
C = np.random.randint(60, size=N) #vector con el que se multiplica
#nueva = [N]

def multiplicar(B, C):
    print("inicia proceso")
    for i in range(N):
        sum = 0
        for j in range(N):
            sum +=B[i][j]*C[j]
            A[i] = sum
    print("Termina proceso de multiplicar")
    print("Resultado de la suma")
    

#def dividirMatriz(B, Pros):
#    nueva = np.split(B, Pros)
#    return nueva

def multiplicar1(B, C, N):
    for i in range(0, int(N/2)):
        sum =0
        for j in range(0, int(N/2)):
            sum +=B[i][j]*C[j]
            A[i] = sum


def multiplicar2(B, C, N):
    for i in range(int(N/2), int(N)):
        sum2 =0
        for j in range(int(N/2), int(N)):
            sum2 +=B[i][j]*C[j]
            A[i] = sum2

if __name__ == '__main__':
    tInit = time.time()
    #p = Process(target=multiplicar, args=(B, C,))

    p1 =Process(target=multiplicar1, args=(B, C,N,))
    p2 =Process(target=multiplicar2, args=(B, C,N,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Tiempo procesos: ", (time.time()-tInit))
    print(A)