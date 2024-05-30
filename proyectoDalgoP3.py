####
####   Proyecto 2 Diseno y Analisis de Algoritmos
####
####   Integrantes y Codigo:
####   Juan Sebastian Ojeda Romero - 202110289
####

import sys
import math

def flip(arr, k):
    left = arr[:k]
    right = arr[k:]
    return left[::-1] + right


def find_max(arr, n):
    return arr.index(max(arr[:n]))


def find_min(arr,n):
    return arr.index(min(arr[:n]))



def es_par(x):
    if (x%2) == 0:
        return True
    else:
        return False

def lemma1_asc(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max(arr, curr_size-1)
        if max_index != curr_size - 1:
            if max_index != 0:
                flip(arr, max_index)
            flip(arr, curr_size - 1)
    return arr


def lemma1_desc(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        min_index = find_min(arr, curr_size-1)
        if min_index != 0:
            flip(arr, min_index)
        flip(arr, curr_size - 1)
    return arr



def pancake_sort(arr):
    cp = int(len(arr)//2)+1
    n = len(arr)
    se = []
    le = []
    aux = []
    A = []
    suma = 0
    B = []
    sumb = 0
    rt = []
    ft = []
    new_arr = arr

    for m in arr:
        i = arr.index(m) + 1
        if (m >= 1) and (m <= (n-cp)):
            se.append(m)
        elif ((cp+1) <= m) and (m<=n):
            le.append(m)

        if (cp < i) and (i <= n):
            aux.append(m)
            rt.append(m)
            
        if (1 <= i) and (i<=cp):
            ft.append(m)


    for y in aux:
        if y in se:
            A.append(y)
            suma += 1
        elif y in le:
            B.append(y)
            sumb += 1
    

    for ele1 in le:
        if suma <= sumb:
            if ele1 in rt:
                rt.remove(ele1)
        else:
            if ele1 in ft:
                ft.remove(ele1)

    for ele2 in se:
        if suma> sumb:
            if ele2 in rt:
                rt.remove(ele2)
        else:
            if ele2 in ft:
                ft.remove(ele2)

    
    if (suma> sumb) and cp in rt:
        rt.remove(cp)
    elif (suma <= sumb) and cp in ft:
        ft.remove(cp)
        
    RSEP = []
    FSEP = []
    for element in rt:
        RSEP.append(arr.index(element)+1)
    for element in ft:
        FSEP.append(arr.index(element)+1)

    k = len(RSEP)

    for pos in range(k,0,-1):

        primer_flip = ft[pos-1]
        new_arr = flip(new_arr,cp-primer_flip)
        new_arr = flip(new_arr,cp)
        new_arr = flip(new_arr,n)
        segundo_flip = rt[k-pos-1]
        if es_par(n) == False:
            new_arr = flip(new_arr,cp-segundo_flip)
            new_arr = flip(new_arr,cp)
        elif es_par(n) == True:
            new_arr = flip(new_arr,cp-segundo_flip-1)
            new_arr = flip(new_arr,cp-1)
        new_arr = flip(new_arr,n)


    if suma <= sumb:
        new_arr = lemma1_asc(new_arr)
        new_arr = flip(new_arr,n)
        new_arr = lemma1_desc(new_arr)
        new_arr = flip(new_arr,n)
    elif suma > sumb:
        new_arr = lemma1_desc(new_arr)
        new_arr = flip(new_arr,n)
        new_arr = lemma1_asc(new_arr)
        new_arr = flip(new_arr,n)

    return new_arr
        



    
    


    

    
        
        

def ordenado(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i + 1]:
            return False
        else:
            i+=1
    return True




def main():
    numero_casos = int(sys.stdin.readline())
    for __ in range(numero_casos):
        lista = []
        case_list = list(map(int, sys.stdin.readline().strip().split()))
        for n in case_list:
            lista.append(n)

        if ordenado(lista):
            print("ORDENADO")
        else:
            print(flip(lista,2))
            print(pancake_sort(lista))
            

main()
    
    


    
