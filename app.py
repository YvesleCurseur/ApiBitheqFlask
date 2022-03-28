from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

# =========================================
#
# Database Shit !
#
# =========================================

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:DeakonCYTY2000@localhost:5432/genesisesag'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Administrateur (db.Model):
    __tablename__='administrateur'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(50), nullable=False)    
    contact = db.Column(db.Integer, nullable=False)
    motdepasse = db.Column(db.String(50), nullable=False)
    motdepasseconfirme = db.Column(db.String(50), nullable=False) 
    typeducompte = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

db.create_all()

@app.route("/")
def index():
    return render_template ("index.html")

@app.route('/creationcompte')
def creationcompte():
    return render_template('create.html')

@app.route("/compte", methods=['POST'])
def compte():
    nom = request.form.get('nom')
    motdepasse = request.form.get('motdepasse')
    typeducompte = request.form.get('typeducompte')
    compte = Administrateur(nom = nom, motdepasse = motdepasse, typeducompte = typeducompte)   
    db.session.add(compte)
    db.session.commit()
    return redirect(url_for('creationcompte'))

@app.route('/comptesdisponibles')
def comptesdisponibles():
    return render_template('account.html', comptes = Administrateur.query.all())
    
@app.route('/contacts')
def contacts():
    return render_template('contact.html')
    
if __name__ == "__main__":
    app.run(debug = True)
