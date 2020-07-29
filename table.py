# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:26:08 2020

@author: KALI CORP
"""

from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    word = Col('Słowo')
    score = Col('Podobieństwo')
    
class Item(object):
    def __init__(self, word, score):
        self.word = word
        self.score = score
