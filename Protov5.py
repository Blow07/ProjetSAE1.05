# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:40:09 2022

@author: boyem
"""

import markdown
with open('test.md.txt',"r") as f:
    text=f.read()
    html=markdown.markdown(text)
    html=html+markdown.markdown(text,extensions=["tables"])
    with open('test.html',"w+") as fff:
        fff.write(html)
print(html)
