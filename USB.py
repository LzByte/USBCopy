import os
import time

diskListF = []
diskListS = []
first = True
c = True

def fun():#Copia los archivos
    pathToCp = (f"{dif[0]}:\\*.*")
    cp=os.popen("powershell cp " + pathToCp + " .\\").read()
    print(cp)


def check(first):
    global FNoDisk
    global NoDisk

    o=os.popen("powershell  gdr -PSProvider 'FileSystem'").readlines()
    if first: #En la primera ejecución guarda el mismo número para evitar errores
        FNoDisk = len(o) - 5
        NoDisk = FNoDisk
    else:
        NoDisk = len(o) - 5
    
    for i in range(NoDisk): #En la primera ejecución guarda la lista de unidades
        disk = o[i + 3]
        print(disk[0])
        if first:
            diskListF.append(disk[0])
        else:
            diskListS.append(disk[0])

check(first)

while c:
    first = False
    time.sleep(3)
    check(first)

    print("--------------")
    print(f"Numero al principio: {FNoDisk} ahora {NoDisk}")
    print("Primera lista:")
    print(diskListF)
    print("Segunda lista:")
    print(diskListS)
    print("--------------")
    
    if NoDisk - FNoDisk == 1: #Checkea si hay diferencia entre el número de unidades inicial y el actual
        print("Diferencia:")
        dif = (list(set(diskListS) - set(diskListF)))
        c = False
        print(dif[0])
        fun()

    else: 
        print("Check")
        diskListS = []
        pass
