# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:17:51 2023

@author: boyem
"""

import datetime
import numpy as np
import matplotlib.pyplot as plt
fichier=open("Dumpfile.txt","r")
texte=fichier.readlines()
for _ in range(len(texte)):
    for i in range(len(texte)):
        if texte[i].startswith("\t"):
            del texte[i]
            break
print(texte)
print("hi")
