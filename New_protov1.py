# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:17:51 2023

@author: boyem
"""
import markdown
import matplotlib.pyplot as plt

fichier=open("Dumpfiletest.txt","r")
texte=fichier.readlines()
fichier.close()
first_len=len(texte)

for _ in range(first_len):
    for i in range(len(texte)):
        if texte[i].startswith("\t"):
            del texte[i]
            break
        
longueur=len(texte)

resultat = [[""] * 1 for _ in range(longueur) ]


colonne=["TIME","IPSRC","IPDST","ICMP","FLAGS","SEQ","ACK",
        "WIN","OPTIONS","LENGTH"]

parameters=["IP",">","ICMP","Flags","seq","ack","win","options","length"]


j=0
for i in range(longueur):
    tes=texte[i].split(" ")
    
    resultat[i][0]=tes[0]
    for chaine in parameters:
        if (chaine in tes)==True and chaine=="ICMP":
            indice_value=tes.index(chaine)
            resultat[i].append(tes[indice_value+2])
        elif (chaine in tes)==True and chaine !="ICMP":
            indice_value=tes.index(chaine)
            resultat[i].append(tes[indice_value+1])
        else:
            resultat[i].append("Vide")    

#Extraction des trajets
chaine_adresse=[]
resultat_adresse_tout=[]
resultat_adresse_nombre=[]
chaine_traite=[]

for i in range(len(resultat)):
    
    if resultat[i][1].startswith("BP"):
        a,b=resultat[i][1].split("."),resultat[i][2].split(".")
        chaine= a[0] + "==>" + b[0]+b[1]+b[2]+b[3]
             
        
    elif resultat[i][2].startswith("BP"):
        a,b=resultat[i][1].split("."),resultat[i][2].split(".")
        chaine= a[0]+a[1]+a[2]+a[3] + "==>" + b[0]
      
    
    resultat_adresse_tout.append(chaine)
    if chaine not in chaine_adresse:
        chaine_adresse.append(chaine)
               
for element in chaine_adresse:
    if element not in chaine_traite:
        resultat_adresse_nombre.append(str(resultat_adresse_tout.count(element)))
        chaine_traite.append(element)
        

#Extraction des flags
flag_type=[]
flag_nombre=[]
flag_traite=[]
for i in range(len(resultat)):
    flags=resultat[i][4]
    if flags not in flag_type:
        flag_type.append(flags)
    flag_traite.append(flags)
for element in flag_type:
    flag_nombre.append(str(flag_traite.count(element)))
        

# Cette manipulation c'est juste pour enlever un \n à la fin de la liste pour resultat[0] et resultat[4]
wrap=resultat[0][-1].split()
resultat[0][-1]=wrap[0]
wrap=resultat[4][-1].split()
resultat[4][-1]=wrap[0]

premiere_ligne_csv=resultat[0]+resultat_adresse_nombre
premiere_ligne_csv.insert(len(colonne), "------")


Entetemax=colonne + chaine_adresse
Entetemax.insert(len(colonne), "------")

# Cas particulier pour bien positionner le tableau flag
cinquieme_ligne=resultat[4] + flag_nombre
cinquieme_ligne.insert(len(colonne), "------")
Entete_ligne_quatre= [ "" for _ in range(11)] + flag_type


# Extraction des données dans le fichier csv 
flag=0      
f = open('TheFichiertest_pour_macro.csv', 'w')
ligneEntete = ";".join(Entetemax) + "\n"
f.write(ligneEntete)
for valeur in resultat:
    if flag==3:
        ligne = ";".join(Entete_ligne_quatre) + "\n"
        f.write(ligne)  
        ligne = ";".join(cinquieme_ligne) + "\n"
        f.write(ligne)
    elif flag==0:
        ligne = ";".join(premiere_ligne_csv) + "\n"
        f.write(ligne)
        flag+=1
    else:
        ligne = ";".join(valeur) + "\n"
        f.write(ligne)
        flag+=1
f.close()

# Importation vers markdown
