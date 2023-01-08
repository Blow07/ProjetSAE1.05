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

resultat = [[""] * 1 for _ in range(longueur) ]

def cherchepour(chaine):
    global valeur,tab_of_event
    for event in texte:
        if event.startswith(chaine):
            tab_of_event=event.split(":")
            valeur=tab_of_event[1]
            break
    return valeur


colonne=["TIME","IPSRC","IPDST","FLAGS","SEQ","ACK",
        "WIN","OPTIONS","LENGTH",]

parameters=["IP",">","Flags","seq","ack","win","options","length"]

print(texte)
j=0
for i in range(longueur):
    tes=texte[i].split()
    
    resultat[i][0]=tes[0]
    if ("IP" in tes)==True:
        indice_value=tes.index("IP")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    if (">" in tes)==True:
        indice_value=tes.index(">")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    if ("Flags" in tes)==True:
        indice_value=tes.index("Flags")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    if ("seq" in tes)==True:
        indice_value=tes.index("seq")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    if ("ack" in tes)==True:
        indice_value=tes.index("ack")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    if ("win" in tes)==True:
        indice_value=tes.index("win")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    if ("options" in tes)==True:
        indice_value=tes.index("options")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    if ("length" in tes)==True:
        indice_value=tes.index("length")
        resultat[i].append(tes[indice_value+1])
    else:
        resultat[i].append("Vide")
    
    
        
        
   
      

print(resultat)

f = open('TheFichier.csv', 'w')
ligneEntete = ";".join(colonne) + "\n"
f.write(ligneEntete)
for valeur in resultat:
     ligne = ";".join(valeur) + "\n"
     f.write(ligne)
f.close() 



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






