from flask import Flask, request, render_template
import pickle
from table import Results
from table import Item
from plots import Full_plot
from tweet_gen import Tweet_generator



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/most_similar')
def most_similar():
    return render_template('most_similar.html')

@app.route('/plots')
def plots():
    return render_template('plots.html')

@app.route('/tweet_gen')
def tweet_gen():
    return render_template('tweet_gen.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    table_pis = ""
    table_ko = ""
    table_lewica = ""
    table_konfederacja = ""
    table_pslkukiz = ""
    
 
    try:
                
        key_word = request.form.get("keyword").lower().replace(" ", "")
        topn = int(request.form.get("topn"))
                                 
        model_pis = pickle.load(open("models/PIS_15-iter_trained_model.sav", "rb"))
        model_ko = pickle.load(open("models/KO_15-iter_trained_model.sav", "rb"))
        model_lewica = pickle.load(open("models/LEWICA_15-iter_trained_model.sav", "rb"))
        model_konfederacja = pickle.load(open("models/KONFEDERACJA_15-iter_trained_model.sav", "rb"))
        model_pslkukiz = pickle.load(open("models/PSL-KUKIZ_15-iter_trained_model.sav", "rb"))
    
        most_similar_pis = model_pis.wv.most_similar(positive=key_word, topn=topn)
        most_similar_ko = model_ko.wv.most_similar(positive=key_word, topn=topn)
        most_similar_lewica = model_lewica.wv.most_similar(positive=key_word, topn=topn)
        most_similar_konfederacja = model_konfederacja.wv.most_similar(positive=key_word, topn=topn)
        most_similar_pslkukiz = model_pslkukiz.wv.most_similar(positive=key_word, topn=topn)
    
        results_pis = []
        for i in range(topn):
            results_pis.append(Item(most_similar_pis[i][0], round(most_similar_pis[i][1],3)))
        results_ko = []
        for i in range(topn):
            results_ko.append(Item(most_similar_ko[i][0], round(most_similar_ko[i][1],3)))
        results_lewica = []
        for i in range(topn):
            results_lewica.append(Item(most_similar_lewica[i][0], round(most_similar_lewica[i][1],3)))
        results_konfederacja = []
        for i in range(topn):
            results_konfederacja.append(Item(most_similar_konfederacja[i][0], round(most_similar_konfederacja[i][1],3)))
        results_pslkukiz = []
        for i in range(topn):
            results_pslkukiz.append(Item(most_similar_pslkukiz[i][0], round(most_similar_pslkukiz[i][1],3)))
    
        table_pis = Results(results_pis)
        table_ko = Results(results_ko)
        table_lewica = Results(results_lewica)
        table_konfederacja = Results(results_konfederacja)
        table_pslkukiz = Results(results_pslkukiz)
           
        return render_template('most_similar.html', table_pis=table_pis, table_ko=table_ko, table_lewica=table_lewica, 
                               table_konfederacja=table_konfederacja, table_pslkukiz=table_pslkukiz, 
                                key_word="Słowo kluczowe: {}".format(key_word), pis="PiS", ko="KO", lewica="Lewica", 
                                konfederacja="Konfederacja", pslkukiz="PSL-Kukiz")
    
    except:
        return render_template('most_similar.html', key_word="Podane słowo nie występuje w słowniku"  )
    
    
@app.route('/fullplot',methods=['POST'])
def fullplot():
    party = request.form.get("party")
    
    if party == "0":
        partyname = "PIS"
    elif party == "1":
        partyname = "KO"
    elif party == "2":
        partyname = "LEWICA"
    elif party == "3":
        partyname = "KONFEDERACJA"
    elif party == "4":
        partyname = "PSL-KUKIZ"
            
    plot = Full_plot.plot_with_matplotlib_full(partyname)
    
  
    return render_template('plots.html', plot=plot)



@app.route('/generate',methods=['POST'])
def generate():
    

    partyname = ""    
    try:
                
        party = request.form.get("party")
        output_num = int(request.form.get("output_num"))
        similar_num = int(request.form.get("similar_num"))
        words = request.form.get("words").lower()
        
        if party == "0":
            partyname = "PIS"
        elif party == "1":
            partyname = "KO"
        elif party == "2":
            partyname = "LEWICA"
        elif party == "3":
            partyname = "KONFEDERACJA"
        elif party == "4":
            partyname = "PSL-KUKIZ"
    
        word_list = []
        
        for word in words.split(","):
            word = word.replace(" ","")
            word_list.append(word)
        
        input_num = len(word_list)
            
        table = Tweet_generator.tweet_gen(input_num, output_num, word_list, similar_num, partyname)
                   
                  
           
        return render_template('tweet_gen.html', table=table, party="Partia: {}".format(partyname), 
                               similar_num="Stopień podobieństwa: {}".format(similar_num), words="słowa zadane: {}".format(words))
    
    except:
        return render_template('tweet_gen.html', table="Jedno z podanych słów nie występuje w słowniku"  )




























if __name__ == "__main__":
    app.run(debug=True)
