# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 00:21:03 2023

@author: boyem
"""

fichier=open("Dumpfile.txt","r")
texte=fichier.readlines()
fichier.close()
longueur=len(texte)
for _ in range(longueur):
    for li in texte:
        if li.startswith("\t"):
            texte.remove(li)
            break
        
print(texte)
    