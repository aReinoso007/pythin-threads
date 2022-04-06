import multiprocessing
import numpy as np
import sys
from multiprocessing import Process
import time 
from numpy import savetxt

#N = int( sys.argv[1])

N = int(25000)
A = np.random.randint(60, size=N) 
B = np.random.randint(60, size=(N,N)) 
C = np.random.randint(60, size=N) 

def multiplicar1(B, C, N):
    for i in range(0, int(N*(1/5))):
        sum =0
        for j in range(0, int(N*(1/5))):
            sum +=B[i][j]*C[j]
            A[i] = sum

def multiplicar2(B, C, N):
    for i in range(int(N*(1/5)), int(N*(2/5))):
        sum2 =0
        for j in range(int(N*(1/5)), int(N*(2/5))):
            sum2 +=B[i][j]*C[j]
            A[i] = sum2

def multiplicar3(B, C, N):
    for i in range(int(N*(2/5)), int(N*(3/5))):
        sum2 =0
        for j in range(int(N*(2/5)), int(N*(3/5))):
            sum2 +=B[i][j]*C[j]
            A[i] = sum2

def multiplicar4(B, C, N):
    for i in range(int(N*(3/5)), int(N*(4/5))):
        sum2 =0
        for j in range(int(N*(3/5)), int(N*(4/5))):
            sum2 +=B[i][j]*C[j]
            A[i] = sum2

def multiplicar5(B, C, N):
    for i in range(int(N*(4/5)), int(N)):
        sum2 =0
        for j in range(int(N*(4/5)), int(N)):
            sum2 +=B[i][j]*C[j]
            A[i] = sum2

def multiplicar(B, C, N1, N2):
    for i in range(int(N1), int(N2)):
        sum2 =0
        for j in range(int(N1), int(N2)):
            sum2 +=B[i][j]*C[j]
            A[i] = sum2

if __name__ == '__main__':
    tInit = time.time()

    p1 =Process(target=multiplicar1, args=(B, C,N,))
    p2 =Process(target=multiplicar2, args=(B, C,N,))
    p3 =Process(target=multiplicar3, args=(B, C,N,))
    p4 =Process(target=multiplicar4, args=(B, C,N,))
    p5 =Process(target=multiplicar5, args=(B, C,N,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    print("Tiempo procesos: ", (time.time()-tInit))
    print("N: ", N)
    print('processor count: ',multiprocessing.cpu_count())
    savetxt('resultadoOperaciones.csv', A, delimiter='[]')
    #print(A)