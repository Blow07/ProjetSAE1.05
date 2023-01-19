# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:56:58 2023

@author: admin
"""

from copy import deepcopy

fichier=open("Dumpfiletest.txt","r")
texte=fichier.readlines()
fichier.close()
def check(x:str):
    if x.startswith("\t"):
        return True
    else:
        return False
filter(check, texte)
        

print(texte)