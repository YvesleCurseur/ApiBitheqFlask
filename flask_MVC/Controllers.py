from flask import request, jsonify
from flask_MVC.Models import Livre, Categorie

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# =========================================
#
#   Basic Index To Showw The Title 
#
# =========================================

def index():
    return "<h1 style = 'position: absolute; top: 45%; left: 15%;'>Welcome to a Flask Api by <a href='https://github.com/YvesleCurseur'>https://github.com/YvesleCurseur<a> !</h1>"

# =========================================
#
#   DATA Livre (show, add)
#
# =========================================

def show_and_add_livre():
    # Show All Livre
    if request.method == "GET":

        livres = Livre.query.all()
        livres = [data.formatLivre() for data in livres]

        return jsonify({
                'Success': True,
                'Livres': livres,
                'Nombre Livre': len(Livre.query.all())
            })
    # Add A Livre
    elif request.method == "POST":

        js = request.get_json()
        visbn = js.get('isbn', None)
        vtitre = js.get('titre', None)
        vdate_publication = js.get('date_publication', None)
        vauteur = js.get('auteur', None)
        vediteur = js.get('editeur', None)
        vcategorie = js.get('categorie_id', None)
        
        rqst = Categorie.query.filter(Categorie.id==vcategorie).all()
        
        if not rqst:
            return jsonify ({"Message" : "La catégorie n'existe pas !"})
        else:
            rqt = Livre.query.filter(Livre.isbn==visbn, Livre.titre==vtitre).all()
            if rqt :
                return jsonify({"Message" : "Le code isbn existe déjà !"})
            elif not rqt :
                livre = Livre(isbn=visbn, titre=vtitre, date_publication=vdate_publication, auteur=vauteur, editeur=vediteur, categorie_id=vcategorie)
                livre.insertLivre()

                livres = Livre.query.all()
                livres_js = [data.formatLivre() for data in livres]

                return jsonify({
                    'Success': True,
                    'Livres': livres_js,
                    'Tous les Livres': len(Livre.query.all())
                })
    # Basic response when everything is wrong   
    else :

        return jsonify({"Message": "Erreur de Requete !"})

# =========================================
#
#   DATA Categorie (show, add)
#
# =========================================

def show_and_add_categorie():
    # Show All Categorie
    if request.method == "GET":

        categories = Categorie.query.all()
        categories = [data.formatCategorie() for data in categories]

        return jsonify({
                'Categories': categories,
                'Nombre Categorie': len(Categorie.query.all())
            })
    # Add A Categorie
    elif request.method == "POST":
    
        js = request.get_json()
        vlibelle_categorie = js.get('libelle_categorie', None)

        if vlibelle_categorie == "":
            return jsonify({"Message" : "Vos champs sont vides !"})
        else :
            rqt = Categorie.query.filter_by(libelle_categorie=vlibelle_categorie).all()
            if rqt :
                return jsonify({"Message" : "La catégorie existe déjà !"})
            elif not rqt :
                categorie = Categorie(libelle_categorie=vlibelle_categorie)
                categorie.insertCategorie()

                categories = Categorie.query.all()
                categories_js = [data.formatCategorie() for data in categories]
                
                return jsonify({
                    'Categories': categories_js,
                    'Toutes les Categories': len(Categorie.query.all())
                })
    # Basic response when everything is wrong   
    else:

        return jsonify({"Message": "Erreur de Requete !"})

# =========================================
#
#   DELETE Livre / Categorie 
#
# =========================================

def delete_livre(livreId):
    # Try and Except for the request error
    try:
        livre=Livre.query.get(livreId)

        if livre is None:
            return jsonify({"Message":"Le livre n'existe pas !"})
        else:
            livre.delete()
            return jsonify({
            'Success':True,
            'id supprime':livreId,
            'Nombre Livre':len(Livre.query.all())
            })
    except:
        return jsonify({"Message": "Erreur de Requete ou code !"})
    finally:
        db.session.close()

def delete_categorie(categorieId):
    # Try and Except for the request error
    try:
        categorie=Categorie.query.get(categorieId)

        if categorie is None:
            return jsonify({"Message":"Le livre n'existe pas !"})
        else:
            categorie.deleteCategorie()
            return jsonify({
            'Success':True,
            'id supprime':categorieId,
            'Nombre Categorie':len(Categorie.query.all())
            })
    except:
        return jsonify({"Message": "Erreur de Requete !"})
    finally:
        db.session.close()






# =========================================
#
#   DATA Livre / Categorie (show by id)
#
# =========================================

def showCategorieId(categorieId):

    categorie = Categorie.query.get(categorieId)

    return jsonify({
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
#   DATA Livre (show livre per categorie)
#
# =========================================

def showLivrePerCategorieId(categorieId):

    # categorie = Categorie.query.get(categorieId)

    # LiCa = Livre.query.filter(Livre.isbn==visbn, Livre.titre==vtitre).all()

    LiCa=Livre.query.filter_by(categorie_id = categorieId).all()
    # LiC=Livre.query.filter_by(categorie_id = categorieId).count()
    # print(LiC)
    Liv = []
    for r in LiCa:
        robj={}
        robj['Categorie'] = r.categorie_id
        robj['Titre'] = r.titre
        robj['Date publication'] = r.date_publication
        robj['Auteur'] = r.auteur
        robj['Editeur'] = r.editeur
        robj['isbn'] = r.isbn
        Liv.append(robj)
    
    return jsonify({
        'Livre' : Liv
        })
    # js = request.get_json()

    # c = js.get('categorie_id', None)
    


    # return jsonify({
    #     'Categorie': LiCa.formatCategorie()
    # })

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
    
    rqst = Categorie.query.filter(Categorie.id==vcategorie).all()
    
    if not rqst:
        return jsonify ({"Message" : "La catégorie n'existe pas !"})
    else:
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

    if vlibelle_categorie == "":
        return jsonify({"Message" : "Vos champs sont vides !"})
    else :
        rqt = Categorie.query.filter_by(libelle_categorie=vlibelle_categorie).all()

        if rqt :
            return jsonify({"Message" : "Cette catégorie existe déjà !"})
        elif not rqt :
            categorie = Categorie(libelle_categorie=vlibelle_categorie)
            categorie.insertCategorie()

            categories = Categorie.query.all()
            categories_js = [data.formatCategorie() for data in categories]
            
            return jsonify({
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

