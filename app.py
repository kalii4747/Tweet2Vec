from flask import Flask, request, render_template
import pickle
from table import Results
from table import Item
#from plots import Full_plot

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', text="Wprowadź dane")

@app.route('/plots')
def plots():
    return render_template('plots.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    table = ""
    partyname = ""    
    try:
        party = request.form.get("party")
        key_word = request.form.get("keyword").lower()
        topn = int(request.form.get("topn"))

        if party == "0":
            model = pickle.load(open("models/PIS_15-iter_trained_model.sav", "rb"))
            partyname = "PIS"
        elif party == "1":
            model = pickle.load(open("models/KO_15-iter_trained_model.sav", "rb"))
            partyname = "KO"
        elif party == "2":
            model = pickle.load(open("models/LEWICA_15-iter_trained_model.sav", "rb"))
            partyname = "LEWICA"
        elif party == "3":
            model = pickle.load(open("models/KONFEDERACJA_15-iter_trained_model.sav", "rb"))
            partyname = "KONFEDERACJA"
        elif party == "4":
            model = pickle.load(open("models/PSL-KUKIZ_15-iter_trained_model.sav", "rb"))
            partyname = "PSL-KUKIZ"
    
        most_similar = model.wv.most_similar(positive=key_word, topn=topn)
    
        results = []
        for i in range(topn):
            results.append(Item(most_similar[i][0], round(most_similar[i][1],3)))
    
        table = Results(results)
           
        return render_template('index.html', table=table,  text="Najbardziej podobne słowa do {} dla {}".format(key_word, partyname))
    
    except:
        return render_template('index.html', table="Podane słowo nie występuje w słowniku"  )
    
    """
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
"""

if __name__ == "__main__":
    app.run(debug=True)
