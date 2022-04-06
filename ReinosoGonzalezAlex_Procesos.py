import multiprocessing
import numpy as np
from multiprocessing import Process
import time
from numpy import savetxt

N = int(100)
A = np.random.randint(60, size=N)
B = np.random.randint(60, size=(N, N))
C = np.random.randint(60, size=N)


def multiplicar(B, C, N1, N2):
    for i in range(int(N1), int(N2)):
        sum2 = 0
        for j in range(int(N1), int(N2)):
            sum2 += B[i][j]*C[j]
            A[i] = sum2


if __name__ == '__main__':
    tInit = time.time()

    p1 = Process(target=multiplicar, args=(B, C, int(0),       int(N*(1/5),)))
    p2 = Process(target=multiplicar, args=(B, C, int(N*(1/5)), int(N*(2/5),)))
    p3 = Process(target=multiplicar, args=(B, C, int(N*(2/5)), int(N*(3/5),)))
    p4 = Process(target=multiplicar, args=(B, C, int(N*(3/5)), int(N*(4/5)), ))
    p5 = Process(target=multiplicar, args=(B, C, int(N*(4/5)), int(N),))

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
    print('processor count: ', multiprocessing.cpu_count())
    savetxt('ReinosoGonzalezAlexResultadoOperaciones.csv', A, delimiter='[]')
    # print(A)
