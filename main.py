from flask import Flask, render_template, request, session, url_for, redirect
from livereload import Server
import random, copy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.debug = True
app.secret_key = b'6hc/_gsh,./;2ZZx3c6_s,1//'
@app.route('/')
def base_page():
    bingo = ["Lapselle viimeinen vaippa", "Onnettomuus", "Pissavahinko", "Lapsen äänekäs pieru", "Aivastus päin", "Lapsi pudottaa ruokaa päällesi", "Kakkaa sormessa", "Lapsi murjoo toista lasta", "Lapsi kutsuu sinua aikuiseksi", "Pyllypesu", "3. muistutus lokeroon", "Lapsi heittää lusikan", "Lapsi tiputtaa mukin", "Pyykkipussi", "Lapsen räkää omissa vaatteissa", "Vanhempi sanoo kiitos"]
    
    bingo1 = copy.deepcopy(bingo)
    bingo2 = copy.deepcopy(bingo)
    bingo3 = copy.deepcopy(bingo)
    bingo4 = copy.deepcopy(bingo)
    random.shuffle(bingo1)
    random.shuffle(bingo2)
    random.shuffle(bingo3)
    random.shuffle(bingo4)
    
    # list random järjestykseen
    # 
    return render_template(
		'alku.html', bingo1 = bingo1, bingo2 = bingo2, bingo3 = bingo3, bingo4 = bingo4
	)

@app.route('/laput',methods = ['POST', 'GET'])
def laput():
    if request.method == 'POST':
        lasku = request.form.to_dict()
        session['taulut'] = "juu"
        return render_template("laskut.html")


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()