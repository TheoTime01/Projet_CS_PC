"""
Created on Tue May 31 8:10:28 2022
@author: Gorvien Mathis / Perrichet Théotime

"""

import multiprocessing as mp
import time

start_time = time.time()

Nb_process = 5

mutex = mp.Semaphore(1)

def arc_tan(n,pi):
    """ Chaque process va calculer une somme de même taille et ajouter celle-ci dans la variable partagée pi
Arguments:
    n : nombre d'itération du process
"""
    somme_Part = 0
    for i in range(n):
        somme_Part += 4/(1+ ((i+0.5)/n)**2)
    mutex.acquire()
    pi.value += (1/n)*somme_Part
    mutex.release()


if __name__ == "__main__" :

    nb_total_iteration = 10**6

    nb_iteration_par_process = nb_total_iteration/Nb_process

    listeProcess = []
    pi = mp.Value('f',0)


    print("Temps d'execution : ", time.time() - start_time)


    for _ in range(Nb_process) :
        process = mp.Process(target = arc_tan, args = (int(nb_iteration_par_process),pi,))
        
        listeProcess.append(process)
        process.start()
    
    for p in listeProcess :
        p.join()

    print("Valeur estimée de Pi par la méthode Multi−process : : ", pi.value)
