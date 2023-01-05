# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:28:55 2022

@author: boyem
"""
import datetime
import numpy as np
fichier=open("Calendar.txt","r")
texte=fichier.read()
tableau=texte.split("\n")




nb_event=tableau.count("BEGIN:VEVENT")
resultat = [[0] * 10 for _ in range(nb_event) ]




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


print(resultat)
    
    

entetes = [
     u'Colonne1',
     u'Colonne2',
     u'Colonne3',
     u'Colonne4',
     u'Colonne5'
]

f = open('monFichier.csv', 'w')
ligneEntete = ";".join(chaine) + "\n"
f.write(ligneEntete)
for valeur in resultat:
     ligne = ";".join(valeur) + "\n"
     f.write(ligne)
f.close() 