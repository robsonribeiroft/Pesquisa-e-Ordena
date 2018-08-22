import matplotlib.pyplot as plt
from random import randint
import timeit
import numpy as np
import scipy.interpolate as interpolate
from threading import Thread

def desenhaGraficoSuave(x,y,l,k,n, xl = "Nº de Elementos", yl = "Tempo(s)"):
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.subplot(n)
    plt.plot(xnew, suave(xnew), label="Curva Suave: "+k)
    #plt.plot(x,y, label="Curva Sem Suaveização: "+k)
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title(l, fontsize=12)
    

def geraLista(tam):
    lista = []
    while(len(lista) < tam):
        n = randint(1,100)
        lista.append(n)
        #if n not in lista: lista.append(n)
    return lista

def listaCrescente(tam):
    lista = []
    for i in range(tam):
        lista.append(i+1)
    return lista

def listaDecrescente(tam):
    lista =[]
    while (tam > 0):
        lista.append(tam)
        tam = tam-1
    return lista

def quickSort(vetor):
    if len(vetor) <= 1: 
        return vetor
    
    pivor = vetor[len(vetor)//2]
    igual = [x for x in vetor if x == pivor]
    esquerda = [x for x in vetor if x < pivor]
    direita = [x for x in vetor if x > pivor]
 
    return quickSort(esquerda) + igual + quickSort(direita)


numsT = [1000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]



def casoMedio(nums0):
    nums = nums0
    time = []
    for r in nums:
        print(r)
        vector = geraLista(r)
        tempo = timeit.timeit("quickSort({})".format(vector),setup="from __main__ import quickSort",number=1)
        time.append(tempo)

    desenhaGraficoSuave(nums, time,'Quick Sort', "Caso Medio",111, "Nº de Elementos", "Tempo(s)")

def piorCaso(nums1):
    nums=nums1
    time1=[]
    for r in nums:
        print (r)
        vector1 = listaDecrescente(r)
        tempo = timeit.timeit("quickSort({})".format(vector1),setup="from __main__ import quickSort",number=1)
        time1.append(tempo)

    desenhaGraficoSuave(nums, time1, 'Quick Sort', "Pior Caso",111, "Nº de Elementos", "Tempo(s)")

def melhorCaso(nums2):
    nums=nums2
    time2=[]
    for r in nums:
        print (r)
        vector1 = listaCrescente(r)
        tempo = timeit.timeit("quickSort({})".format(vector1),setup="from __main__ import quickSort",number=1)
        time2.append(tempo)

    desenhaGraficoSuave(nums, time2, 'Quick Sort', "Melhor Caso",111, "Nº de Elementos", "Tempo(s)")


casoMedio(numsT)
piorCaso(numsT)
melhorCaso(numsT)
plt.show()

