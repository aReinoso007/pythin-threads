import multiprocessing
import threading
import numpy as np
import sys
import time 
from multiprocessing import Process
from threading import Thread

#N = int( sys.argv[1])
N = 1000
A = np.random.randint(60, size=N) #para guardar el resultado
B = np.random.randint(60, size=(N,N)) #la matriz con la que se debe multiplicar
C = np.random.randint(60, size=N) #vector con el que se multiplica

def multiplicacionParalela(inicio, final):
    for i in range(inicio, final):
        sum =0
        for j in range(N):
            for k in range(N):
                sum +=B[i][j]*C[j]
                A[j] = sum

def hilos():
    numeroHilos = 5
    thread_handle = []

    for j in range(0, numeroHilos):
        t = Thread(target=multiplicacionParalela, args=(int((N/numeroHilos) * j),int((N/numeroHilos) * (j+1))))
        thread_handle.append(t)
        t.start()
        
        for j in range(0, numeroHilos):
            thread_handle[j].join()

if __name__=="__main__":
    tInit = time.time()
    hilos()
    print("Tiempo procesos: ", (time.time()-tInit))
    print(A)