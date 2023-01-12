# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:42:43 2023

@author: boyem
"""

fichier=open("Dumpfiletest.txt","r")
lignes=fichier.readlines()

for ligne in lignes:
    if ligne.startswith("\t"):
        print(ligne)
