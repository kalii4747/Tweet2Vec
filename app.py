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
    
    table = ""
    partyname = ""    
    try:
                
        party = request.form.get("party")
        key_word = request.form.get("keyword").lower().replace(" ", "")
        topn = int(request.form.get("topn"))
        
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

                    
        model = pickle.load(open("models/" + partyname + "_15-iter_trained_model.sav", "rb"))
    
        most_similar = model.wv.most_similar(positive=key_word, topn=topn)
    
        results = []
        for i in range(topn):
            results.append(Item(most_similar[i][0], round(most_similar[i][1],3)))
    
        table = Results(results)
           
        return render_template('most_similar.html', table=table,  text="Najbardziej podobne słowa do {} dla {}".format(key_word, partyname))
    
    except:
        return render_template('most_similar.html', table="Podane słowo nie występuje w słowniku"  )
    
    
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
                   
                  
           
        return render_template('tweet_gen.html', table=table,  text="Tweet wygenerowany dla {}".format(partyname))
    
    except:
        return render_template('tweet_gen.html', table="Jedno z podanych słów nie występuje w słowniku"  )




























if __name__ == "__main__":
    app.run(debug=True)
