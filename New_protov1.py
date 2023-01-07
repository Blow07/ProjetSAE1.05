# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:17:51 2023

@author: boyem
"""
import markdown
import datetime
import numpy as np
import matplotlib.pyplot as plt
fichier=open("Dumpfile.txt","r")
texte=fichier.readlines()
fichier.close()
for _ in range(len(texte)):
    for i in range(len(texte)):
        if texte[i].startswith("\t"):
            del texte[i]
            break
longueur=len(texte)

    
print(f"{longueur=}")

resultat = [[""] * 21 for _ in range(longueur) ]

def cherchepour(chaine):
    global valeur,tab_of_event
    for event in texte:
        if event.startswith(chaine):
            tab_of_event=event.split(":")
            valeur=tab_of_event[1]
            break
    return valeur


colonne=["TIME","IPSRC","","IPDST","FLAGS","SEQ","ACK",
        "WIN","OPTIONS","LENGTH",]

print(texte)
j=0
for i in range(longueur-1):
    tes=texte[i].split()
    print(tes)
    for j in range(len(tes)):
       resultat[i][j]=tes[j]
    j=0
   
      
print(resultat)  
for i in range(longueur-1):
    resultat[i].remove('win')
print(resultat)


""" 

test=texte[0].split()
to_remove=[1,2,3,4,5,6,7,12]
to_fuse=[7,7,7,7,7] 


for element in to_remove:
    del test[element]
    print(test)
    print("\n")

element_to_fuse=[]
for i in to_fuse:
    element_to_fuse.append(test.pop(i))
test.insert(-1,"-".join(element_to_fuse))
print(test)


"""




