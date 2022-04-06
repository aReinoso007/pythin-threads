import numpy as np
import time
from random import randint
from numpy import savetxt

N = 20000
A = np.random.randint(60, size=N) 
B = np.random.randint(60, size=(N,N)) 
C = np.random.randint(60, size=N) 

start = time.time()
for i in range(N):
    sum = 0
    for j in range(N):
        sum += B[i][j] * C[j]
        A[i] = sum

print("Tiempo Secuencial: ", (time.time() - start))
savetxt('ReinosoGonzalezAlexResultadoSecuencial.csv', A, delimiter=' ')