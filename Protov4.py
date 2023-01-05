# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:34:51 2022

@author: boyem
"""
import datetime
import numpy as np
import matplotlib.pyplot as plt
fichier=open("Calendar.txt","r")
texte=fichier.read()
tableau=texte.split("\n")




nb_event=tableau.count("BEGIN:VEVENT")
resultat = [[0] * 10 for _ in range(nb_event) ]

nb_r107=tableau.count("SUMMARY:R107")
tab_r107 = [[0] * 10 for _ in range(nb_r107-2) ]



def cherchepour(chaine):
    global valeur,tab_of_event
    for event in tableau:
        if event.startswith(chaine):
            tab_of_event=event.split(":")
            valeur=tab_of_event[1]
            break
    return valeur
 
          
chaine=["DTSTAMP","DTSTART","DTEND","SUMMARY","LOCATION","DESCRIPTION","UID",
        "CREATED","LAST-MODIFIED","SEQUENCE",]


j=0
for i in range(nb_event):
    for element in chaine:
        if cherchepour(element)=="":
            resultat[i][j]="vide"
            j+=1
        else:
            resultat[i][j]=cherchepour(element)
            j+=1
    for i in range(11):
        tableau.pop(i)
    j=0


j=0
for i in range(len(resultat)):
    if resultat[i][3]=="R107":
        tab_r107[j]=resultat[i]
        j+=1
  
   


f = open('r107.csv', 'w')
ligneEntete = ";".join(chaine) + "\n"
f.write(ligneEntete)
for valeur in tab_r107:
     ligne = ";".join(valeur) + "\n"
     f.write(ligne)
f.close() 


nb_tp_dec=0
nb_tp_nov=0
nb_tp_oct=0
nb_tp_sept=0
for i in range(len(resultat)):
    if ("202112" in resultat[i][1])==True and ("RT1-TP" in resultat[i][5])==True:
        nb_tp_dec+=1
    elif ("202111" in resultat[i][1])==True and ("RT1-TP" in resultat[i][5])==True:
        nb_tp_nov+=1
    elif ("202110" in resultat[i][1])==True and ("RT1-TP" in resultat[i][5])==True:
        nb_tp_oct+=1
    elif ("202109" in resultat[i][1])==True and ("RT1-TP" in resultat[i][5])==True:
        nb_tp_sept+=1
        
        
        
        


labels = ["Septembre", "Octobre", "Novembre", "Décembre"]
sizes = [nb_tp_sept, nb_tp_oct, nb_tp_nov, nb_tp_dec]
colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral"]
plt.pie(sizes, labels=labels, colors=colors,
autopct="%1.1f%%", shadow=True, startangle=90)
plt.axis("equal")
plt.savefig("PieChart01.png")
plt.show()