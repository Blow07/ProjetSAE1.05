# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:17:51 2023

@author: boyem
"""
import markdown
import matplotlib.pyplot as plt

fichier=open("Dumpfile.txt","r")
texte=fichier.readlines()
fichier.close()
first_len=len(texte)
second_len=first_len

for _ in range(first_len):
    for i in range(second_len):
        if texte[i].startswith("\t"):
            del texte[i]
            second_len-=1
            break
        
longueur=second_len

        

resultat = [[""] * 1 for _ in range(longueur) ]


colonne=["TIME","IPSRC","IPDST","ICMP","FLAGS","SEQ","ACK",
        "WIN","OPTIONS","LENGTH"]

parameters=["IP",">","ICMP","Flags","seq","ack","win","options","length"]


# On split les entetes par des espaces et on récupérer la valeur voulu qui est positionné a l'indice suivant sauf pour icmp qui est un cas particulier.
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
    
    # Pour ce déparasser des ports on utilise un split(".") sauf pour BPlinux
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
    
    
# Extraction adreesse+ flag
adresse_flag_traite=[]
adresse_flag=[]
adresse_flag_nombre=[]

for i in range(len(resultat)):
    
    ad_source=resultat[i][1].split(".")
    ad_source=ad_source[0]
    if ad_source+"&"+resultat[i][4] not in adresse_flag:
        adresse_flag.append(ad_source+"&"+resultat[i][4])
    adresse_flag_traite.append(ad_source+"&"+resultat[i][4])
        
for element in adresse_flag:
    adresse_flag_nombre.append(str(adresse_flag_traite.count(element)))

    
   
        
# Cette manipulation c'est juste pour enlever un \n à la fin de la liste pour resultat[0] et resultat[4]
wrap=resultat[0][-1].split()
resultat[0][-1]=wrap[0]
wrap=resultat[4][-1].split()
resultat[4][-1]=wrap[0]

premiere_ligne_csv=resultat[0]+resultat_adresse_nombre
premiere_ligne_csv.insert(len(colonne), "")


Entetemax=colonne + chaine_adresse
Entetemax.insert(len(colonne), "")

# Cas particulier pour bien positionner le tableau flag
cinquieme_ligne=resultat[4] + flag_nombre
cinquieme_ligne.insert(len(colonne), "")
Entete_ligne_quatre= [ "" for _ in range(11)] + flag_type


neuviéme_ligne=resultat[8]+adresse_flag_nombre
huitiéme_ligne=["" for i in range(11)] + adresse_flag
neuviéme_ligne.insert(len(colonne), "") 


# Extraction des données dans le fichier csv 
flag=0      
f = open('CSV_file_vFINAL.csv', 'w')
ligneEntete = ";".join(Entetemax) + "\n"
f.write(ligneEntete)
for valeur in resultat:
    if flag==3:
        ligne = ";".join(Entete_ligne_quatre) + "\n"
        f.write(ligne)  
        ligne = ";".join(cinquieme_ligne) + "\n"
        f.write(ligne)
    if flag==0:
        ligne = ";".join(premiere_ligne_csv) + "\n"
        f.write(ligne)
        flag+=1
    if flag==8:
        ligne = ";".join(huitiéme_ligne) + "\n"
        f.write(ligne)
        ligne = ";".join(neuviéme_ligne) + "\n"
        f.write(ligne)
        flag+=1
    else:
        ligne = ";".join(valeur) + "\n"
        f.write(ligne)
        flag+=1
f.close()

# Création des graphiques

# Diagramme circulaire trajets
labels = chaine_adresse
sizes = resultat_adresse_nombre
plt.pie(sizes, labels=labels, 
autopct="%1.1f%%", shadow=True, startangle=90)
plt.axis("equal")
plt.legend()
plt.savefig("PieChart01.png")
plt.show()


# Diagramme à barres flags
x = []
for i in range(len(flag_type)):
    x.append(i+1)
y = flag_nombre
labels = flag_type
plt.bar(x,y, tick_label = labels,
width = 0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('My bar chart!')
plt.savefig("PieChart02.png")
plt.show()

#Diagramme à barres adresse et flags
x = []
for i in range(len(adresse_flag)):
    x.append(i+1)
y = adresse_flag_nombre
labels = adresse_flag
plt.bar(x,y, tick_label = labels,
width = 0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('My bar chart!')
plt.savefig("PieChart03.png")
plt.show()


# Importation vers markdown
fm= open("test.md","w+")
fm.write(""" # Extraction des donnees
         ![img1](../ProjetSAE1.05/PieChart01.png)
 ![img2](../ProjetSAE1.05/PieChart02.png)
 ![img3](../ProjetSAE1.05/PieChart03.png)
 #How to use the Tcp_dump_file_extraction:


Warning: This program can only extract informations from a tcp dump file, you can't use it for another type of file

==================================================================================================================

Before to run make sure that the programme and the tcp dump file are located on the same folder.
You must also rename your file "Dumpfile" ( it should have the .txt enxtension).
The programm is a python file, you can interpret it with a IDE or with your local python environement like
conda or anaconda. 
After you run it, the programm will make some time to extract all the data depending on the tcp-dump-file's size (~10mn if your file is higher than 25mo)

=================================================================================================================

After the programm is done you will get some files:
-------------------------------------------------

* Markdown file : You can delete it, it was just for making the html file
* HTML file : The graphics are exported in a html file
* CSV_file : The information are exported in csv file with 4 tables:
			¤ In the first table you have all the informations from the header of the frames ( Time,IPSRC,IPDST,SEQ,ACK,WIN.....)
			¤ In the second table all the routes (IPSRC==IPDST)
			¤ In the third table all the flags
			¤ In the fourth you have a combination of the routes and flags
---------------------------------------------------

To make appear the graphic you can do it manually or use the Macro file which accompanies the programm:

Open the macro_file in the folder macro and the csv file, enable the developper mode ( go to file --> more --> options --> ruaban --> check the developper mode)

Then go to macro and run the macro or use this shortcut : Ctrl+Shift+M

If you have this following error: "Becausse to your security...." Please go to the macro setting on the both file and make sure than the Enable all macro is checked,
try to reopen the file after that.

With this macro you'll have The 3 graphics of the TCP_dump_file

Here are some info on the acronym of the tcp flags:
Acronym 	Name 	Meaning
SYN 	Synchronization 	Used to create a TCP connection
ACK 	Acknowledgment 	Used to acknowledge the reception of data or synchronization packets
PSH 	Push 	Instruct the network stacks to bypass buffering
URG 	Urgent 	Indicates out-of-band data that must be processed by the network stacks before normal data
FIN 	Finish 	Gracefully terminate the TCP connection
RST 	Reset 	Immediately terminate the connection and drop any in-transit data

Thanks for reading""")
fm.seek(0)
text=fm.read()
html=markdown.markdown(text)
print(html)
fh= open("Exportation.html","w+")
fh.write(html)
fm.close()
fh.close()