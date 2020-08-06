# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:07:46 2020

@author: KALI CORP
"""

import pickle
import plotly
import plotly.graph_objs as go
import json
import numpy as np

class Full_plot():
    
    def plot_with_matplotlib_full(party):
    
        filename = "models/" + party + "_15-iter_reduced_model.sav"

        loaded_reduced_model = pickle.load(open(filename, "rb"))

        x_vals, y_vals, labels = loaded_reduced_model
    
        new_dictionary = ["konstytucja", "prawo", "kościół", "ksiądz", "aborcja", "rodzina", 
                  "polska", "kraj", "europa", "unia", "rosja", "niemcy", "usa", "francja",
                  "pis", "platforma", "lewica", "konfederacja", "kukiz", "psl",
                  "kaczyński", "morawiecki", "tusk", "komunizm", "faszyzm", "nacjonalizm",
                  "patriotyzm", "my", "oni", "koalicja", "opozycja", "kłamstwo",
                  "socjalizm", "premier", "prezydent", "duda", "minister", "invitro",
                  "świat", "europa", "zachód", "suwerennoć", "putin", "merkel",
                  "orban", "silny", "słaby", "zdrajca", "kłamstwo", "kłamać",
                  "lider", "wódz", "szkodliwy", "bezpieczny", "wspólnota", 
                  "imigrant", "tradycja", "przemysł", "pokój", "wojna",
                  "ameryka", "elektorat", "biedroń", "korwin", "demokracja", "postkomunista",
                  "socjalista", "układ", "kosiniak", "sojusz", "federacja", "jednopłciowy",
                  "wielodzietny", "godny", "katolicki", "sakrament", "pedofilia",
                  "homoseksualny", "biskup", "pedofil", "papież", "wyznaniowy", "molestować",
                  "liberalizacja", "liberalizować", "traktat", "brexit", "parlament",
                  "zły", "dobry", "totalitarny", "totalitaryzm", "sowiecki", "patologiczny",
                  "ksenofobia", "chrzecijaństwo", "agresja", "wielokultorowość",
                  "antysemityzm", "terroryzm", "lewacki", "agresja", "trzaskowski", "kidawa", 
                  "korespondencyjny", "covid", "koronawirus", "wybory", "lgbt", "eutanazja",
                  "ojczyzna", "wirus", "epidemia", "rozprzestrzeniać", "pandemia", "sars", 
                  "test", "zalażenie", "nosiciel", "pseudowybory", "pkw", "głosowanie",
                  "zawetować", "ideologia", "gej", "lesbijka", "gender", "dyskryminacja",
                  "szczuć", "orientacja", "deficyt", "lewacki", "tolerancja", "sasin",
                  "drukować", "poczta", "trump", "obama", "kopertowy", "aktywista", 
                  "lobby", "proaborcyjny", "deprawacja", "dewiacja", "demoralizacja", "tęczowy",
                  "ziobro", "hołownia", "praworządność", "kurski", "tvp", "propagandysta",
                  "propaganda", "telewizja", "szczujnia", "tępy", "tv", "onkologia",
                  "miliard", "idiota", "polak", "naród", "złodziej", "oszust", "prezes",
                  "komunista", "kiszczak", "jaruzelski", "zbrodniarz", "wałęsa", "gaz"]
        #print("dict done")
    
        new_labels = []
        new_x_vals = []
        new_y_vals = []

        for word in labels:
            if word in new_dictionary:
                index = np.where(labels==word)[0][0]

                new_labels.append(word)
                new_x_vals.append(x_vals[index])
                new_y_vals.append(y_vals[index])
        
        
        
        
        data = [go.Scatter(
            x = new_x_vals,
            y = new_y_vals,
            text = new_labels,
            textposition='top center',
            mode = 'markers+text'
        )]


        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
