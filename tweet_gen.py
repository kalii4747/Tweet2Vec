# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:11:53 2020

@author: KALI CORP
"""

import pickle




        
class Tweet_generator():

    def tweet_gen(input_words_num, total_words_num, word_list, similar_num, party):
        
        filename = "models/" + party + "_15-iter_trained_model.sav"
        loaded_model = pickle.load(open(filename, "rb"))
        
        
        if input_words_num == 1:
            
            most_similar = loaded_model.wv.most_similar (positive=word_list[0])
            word_list.append(most_similar[similar_num-1][0])
            
            for i in range(2,total_words_num):
                
    
                predicted_word = loaded_model.wv.most_similar (positive=word_list)
  
                next_word = predicted_word[similar_num-1][0]
                if next_word in word_list:
                    next_word = predicted_word[similar_num][0]
                    
                word_list.append(next_word)
   
    
            
        elif input_words_num > 1: 
            
            for i in range(input_words_num,total_words_num):
                
                predicted_word = loaded_model.wv.most_similar (positive=word_list)
                next_word = predicted_word[similar_num-1][0]
                if next_word in word_list:
                    next_word = predicted_word[similar_num][0]
                 
                word_list.append(next_word)
    
        sentence = ""
        for word in word_list:
            sentence = sentence + word + " "
            
        return sentence
        


