from flask import*
from googletrans import Translator
import spacy    
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/translator")
def translator():
    return render_template("index.html")

@app.route("/translate",methods=["POST"])
def translate():
    if request.method=="POST":
        t=Translator()
        txt1=request.form["a"]
        txt2=request.form['b']
        txt3=request.form['txtarea']
        res=t.translate(txt3,src=txt1,dest=txt2)
        return render_template('index.html',r=res.text)
    return redirect(url_for('translator'))

@app.route("/pos")
def pos():
    return render_template("pos.html")

@app.route("/part_of_speech",methods=["POST"])
def part_of_speech():
    if request.method=="POST":
        a=request.form['txt']
        nlp=spacy.load('en_core_web_sm')
        text=a
        doc=nlp(u"{}".format(text))
        l=[]
        for i in doc:
            pr=f"{i.text} : {spacy.explain(i.pos_)}"
            l.append(pr)
        return render_template("pos.html",p=l)
    redirect(url_for('pos'))

@app.route("/profile")
def profile():
    return render_template("index2.html")

    
if __name__=="__main__":
    app.run()
