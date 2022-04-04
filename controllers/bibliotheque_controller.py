import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.bibliotheque import Livre, Categorie
from sqlalchemy import select

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# =========================================
#
# Test Json respon
#
# =========================================

def index():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

# =========================================
#
#   DATA Livre / Categorie (show)
#
# =========================================

def showLivre():

    livres = Livre.query.all()
    livres = [data.formatLivre() for data in livres]

    return jsonify({
            'Success': True,
            'Livres': livres,
            'Nombre Livre': len(Livre.query.all())
        })

def showCategorie():

    categories = Categorie.query.all()
    categories = [data.formatCategorie() for data in categories]

    return jsonify({
            'Categories': categories,
            'Nombre Categorie': len(Categorie.query.all())
        })

# =========================================
#
#   DATA Livre / Categorie (show by id)
#
# =========================================

def showCategorieId(categorieId):

    categorie = Categorie.query.get(categorieId)
    return jsonify({
        'Success': True,
        'id': categorieId,
        'Categorie': categorie.formatCategorie()
    })

def showLivreId(livreId):
    try:
        Li=db.session.query(Categorie,Livre).join(Livre).filter(Livre.id==livreId).all()
        
        Liv = []

        for r in Li:
            robj={}
            robj['Categorie'] = r.Categorie.libelle_categorie
            robj['Titre'] = r.Livre.titre
            robj['Date publication'] = r.Livre.date_publication
            robj['Auteur'] = r.Livre.auteur
            robj['Editeur'] = r.Livre.editeur
            robj['isbn'] = r.Livre.isbn

            Liv.append(robj)
        
        return jsonify({
            'Livre' : robj
        })
    except:
        return jsonify({"Message" : "Ce livre n'existe pas !"})

# =========================================
#
#   INSERT Livre / Categorie (store)
#
# =========================================

def storeLivre():

    js = request.get_json()
    visbn = js.get('isbn', None)
    vtitre = js.get('titre', None)
    vdate_publication = js.get('date_publication', None)
    vauteur = js.get('auteur', None)
    vediteur = js.get('editeur', None)
    vcategorie = js.get('categorie_id', None)

    rqt = Livre.query.filter(Livre.isbn==visbn, Livre.titre==vtitre).all()

    if rqt :
        return jsonify({"Message" : "Ce code isbn existe déjà !"})
    elif not rqt :
        livre = Livre(isbn=visbn, titre=vtitre, date_publication=vdate_publication, auteur=vauteur, editeur=vediteur, categorie_id=vcategorie)
        livre.insertLivre()

        livres = Livre.query.all()
        livres_js = [data.formatLivre() for data in livres]

        return jsonify({
            'Livres': livres_js,
            'Tous les Livres': len(Livre.query.all())
        })

def storeCategorie():

    js = request.get_json()
    vlibelle_categorie = js.get('libelle_categorie', None)

    rqt = Categorie.query.filter_by(libelle_categorie=vlibelle_categorie).all()

    if rqt :
        return jsonify({"Message" : "Cette catégorie existe déjà !"})
    elif not rqt :
        categorie = Categorie(libelle_categorie=vlibelle_categorie)
        categorie.insertCategorie()

        categories = Categorie.query.all()
        categories_js = [data.formatCategorie() for data in categories]
        
        return jsonify({
            'success': True,
            'idCategorie': categorie.id,
            'Categories': categories_js,
            'Toutes les Categories': len(Categorie.query.all())
        })

# =========================================
#
#   UPDATE Livre / Categorie (store)
#
# =========================================

def editCategorie(categorieId):

    js = request.get_json()
    Ca = Categorie.query.filter(Categorie.id == categorieId).one_or_none()
    Ca.libelle_categorie = js.get('libelle_categorie')
    Ca.updateCategorie()
    return jsonify({
        # 'Livre': ""
        'Libellé categorie': Ca.formatCategorie()
    })

def editLivre(livreId):

    js = request.get_json()
    Li = Livre.query.filter(Livre.id == livreId).one_or_none()

    Li.isbn = js.get('isbn')
    Li.titre = js.get('titre')
    Li.date_publication = js.get('date_publication')
    Li.auteur = js.get('auteur')
    Li.editeur = js.get('editeur')
    Li.categorie_id = js.get('categorie_id')

    Li.updateLivre()

    return jsonify({
        'Libellé categorie': Li.formatLivre()
    })

