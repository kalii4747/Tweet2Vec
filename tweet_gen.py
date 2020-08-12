# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:11:53 2020

@author: KALI CORP
"""

import pickle



# print("\n Dla jakiej partii chcesz wygenerować tweet?")
# party = (str(input())).upper()

# filename = "models/" + party + "_15-iter_trained_model.sav"
# loaded_model = pickle.load(open(filename, "rb"))


# print("\n Podaj liczbę słów wejciowych:")
# input_words_num = int(input())

# print("\n Podaj oczekiwaną liczbę słów w zdaniu:")
# total_words_num = int(input())

# print("\n Które w kolejnoci najbliższe słowo ma zostać wygenerowane jako następne? Podaj liczbę większą od 0.")
# n = int(input())


# word_list = []

# if input_words_num == 1:
    
#     print("\n Podaj pierwsze słowo:")

#     first_word = str(input())
#     word_list.append(first_word)
    
# elif input_words_num > 1: 
    
#     for i in range(0, input_words_num):
        
#         print("\n Podaj " + str(i+1) + " słowo:")

#         word = str(input())
#         word_list.append(word)
        
class Tweet_generator():

    def tweet_gen(input_words_num, total_words_num, word_list, similar_num, party):
        
        filename = "models/" + party + "_15-iter_trained_model.sav"
        loaded_model = pickle.load(open(filename, "rb"))
        
        
        if input_words_num == 1:
            
            most_similar = loaded_model.wv.most_similar (positive=word_list[0])
            word_list.append(most_similar[similar_num-1][0])
            
            for i in range(2,total_words_num):
                
    
                predicted_word = loaded_model.wv.most_similar (positive=word_list)
    #            print(predicted_word)
                next_word = predicted_word[similar_num-1][0]
                if next_word in word_list:
                    next_word = predicted_word[similar_num][0]
                    
                word_list.append(next_word)
    #            print(word_list)
    
            
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
        # print("\n" + sentence)
    
    
    
    

#Tweet_generator.tweet_gen(input_words_num, total_words_num, word_list)



