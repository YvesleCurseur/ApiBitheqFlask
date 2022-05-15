from flask import request, jsonify, abort, session
from src.models import Livre, Categorie

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
#   DATA Categorie (show, add)
#
# =========================================


def show_and_add_category():
    # Message error for the function not working
    try:
        # Mauvaise méthode
        try:
            # Show All Categorie
            if request.method == "GET":
                # Mauvaise requête
                try:
                    categories = Categorie.query.all()
                    categories = [data.formatCategorie() for data in categories]

                    return jsonify({
                        'Success': True,
                        'Categories': categories,
                        'Nombre Categorie': len(categories)
                    })
                except:
                    abort(400)
        except:
            # Method is wrong
            abort(405)
        finally:
            db.session.close()

        try:
            # Add A Categorie
            if request.method == "POST":
                try:
                    js = request.get_json()
                    vlibelle_categorie = js.get('libelle_categorie', None)

                    if vlibelle_categorie == "":
                        return jsonify({
                            "Success": False,
                            "Message": "Vos champs sont vides !"
                        })
                    else:
                        rqt = Categorie.query.filter_by(
                            libelle_categorie=vlibelle_categorie).all()
                        if rqt:
                            return jsonify({
                                "Success": False,
                                "Message": "La catégorie existe déjà !"
                            })
                        elif not rqt:
                            session['libelle_categorie']=vlibelle_categorie
                            categorie = Categorie(
                                libelle_categorie=vlibelle_categorie)
                            categorie.insertCategorie()

                            categories = Categorie.query.all()
                            categories_js = [data.formatCategorie()
                                            for data in categories]

                            return jsonify({
                                'Success': True,
                                'Categorie': categories_js,
                                'Nombre Categorie': len(categories)
                            })
                except:
                    abort(400)
        except:
            # Method is wrong
            abort(405)
        finally:
            db.session.close()

    # Basic response when everything is wrong (will transform in json) Bad
    # request
    except:
        abort(404)

# =========================================
#
#   DATA Livre (show, add)
#
# =========================================


def show_and_add_book():
    # Message error for the function not working
    try:

        try:
            # Show All Livre
            if request.method == "GET":
                try:
                    livres = Livre.query.all()
                    livres = [data.formatLivre() for data in livres]

                    return jsonify({
                        'Success': True,
                        'Livres': livres,
                        'Nombre Livre': len(livres)
                    })
                except:
                    abort(400)
        except:
            # Method is wrong
            abort(405)

        try:
            # Add A book
            if request.method == "POST":
                try:
                    # Recupère les données envoyées en json
                    js = request.get_json()

                    # Recupère chaque infos sous forme json (s'assurer que le
                    # champs soit nullable pour utiliser none)
                    visbn = js.get('isbn', None)
                    vtitre = js.get('titre', None)
                    vdate_publication = js.get('date_publication', None)
                    vauteur = js.get('auteur', None)
                    vediteur = js.get('editeur', None)
                    vcategorie = js.get('categorie_id', None)

                    rqst = Categorie.query.filter(Categorie.id == vcategorie).all()

                    if not rqst:
                        return jsonify({
                            "Success": False,
                            "Message": "La catégorie n'existe pas !"
                        })
                    else:
                        rqt = Livre.query.filter(
                            Livre.isbn == visbn, Livre.titre == vtitre).all()
                        if rqt:
                            return jsonify({
                                "Success": False,
                                "Message": "Le code isbn existe déjà !"
                            })
                        elif not rqt:
                            livre = Livre(
                                isbn=visbn,
                                titre=vtitre,
                                date_publication=vdate_publication,
                                auteur=vauteur,
                                editeur=vediteur,
                                categorie_id=vcategorie)
                            livre.insertLivre()

                            livres = Livre.query.all()
                            livres_js = [data.formatLivre() for data in livres]

                            return jsonify({
                                'Success': True,
                                'Livre': livres_js,
                                'id Livre': livre.id,
                                'Nombre Livre': len(livres)
                            })
                except:
                    abort(400)
        except:
            # Method is wrong
            abort(405)
        finally:
            db.session.close()

    # Basic response when everything is wrong (will transform in json) Bad
    # request
    except:
        abort(404)

# =========================================
#
#   DATA Livre(id) (update, delete)
#
# =========================================


def update_and_delete_book_id(livreId):

    try:

        try:
            if request.method == "DELETE":
                try:
                    livre = Livre.query.get(livreId)

                    # None => id not found
                    if livre is None:
                        return jsonify({
                            "Success": False,
                            "Message": "Le livre n'existe pas !"
                        })
                    else:
                        livre.deleteLivre()
                        livres = Livre.query.all()
                        return jsonify({
                            'Success': True,
                            'Id Livre': livreId,
                            'Nombre Livre': len(livres)
                        })
                except:
                    abort(400)
        except:
            abort(405)
        finally:
            db.session.close()

        try:
            if request.method == "PATCH":
                try:
                    js = request.get_json()
                    livre = Livre.query.get(livreId)
                    livres = Livre.query.all()

                    if livreId is None:
                        return jsonify({
                            "Success": False,
                            "Message": "Le livre n'existe pas !"
                        })
                    else:

                        livre.isbn = js.get('isbn', None)
                        livre.titre = js.get('titre', None)
                        livre.date_publication = js.get('date_publication', None)
                        livre.auteur = js.get('auteur', None)
                        livre.editeur = js.get('editeur', None)
                        livre.categorie = js.get('categorie_id', None)

                        rqt = Livre.query.filter(Livre.isbn == livre.isbn,Livre.titre == livre.titre).all()
                        if rqt is not None:
                            return jsonify({
                                "Success": False,
                                "Message": "Le code isbn existe déjà !"
                            })
                        
                        livre.updateLivre()

                        return jsonify({
                            'Success': True,
                            'Livre': livre.formatLivre(),
                            'Nombre Livre': len(livres)
                        })
                except:
                    abort(400)
        except:
            abort(405)
        finally:
            db.session.close()

    except:
        abort(404)
# =========================================
#
#   DATA Categorie(id) (update, delete)
#
# =========================================


def update_and_delete_category_id(categorieId):
    # Mauvais lien pour un not found
    try:

        try:
            # delete a categorie
            if request.method == "DELETE":
                try:
                    categorie = Categorie.query.get(categorieId)

                    if categorie is None:
                        return jsonify({
                            "Success": False,
                            "Message": "La categorie n'existe pas !"
                        })
                    else:
                        categorie.deleteCategorie()
                        categories = Categorie.query.all()
                        return jsonify({
                            'Success': True,
                            'id supprime': categorieId,
                            'Nombre Categorie': len(categories)
                        })
                except:
                    abort(400)
        except:
            abort(405)
        finally:
            db.session.close()
        # Mauvaise méthode
        try:
            if request.method == "PATCH":
                # Mauvaise requête
                try:
                    js = request.get_json()
                    categorie = Categorie.query.get(categorieId)
                    categories = Categorie.query.all()

                    if categorieId is None:
                        return jsonify({
                            "Success": False,
                            "Message": "La categorie n'existe pas !"
                        })
                    else:
                        categorie.libelle_categorie = js.get('libelle_categorie', None)

                        if categorie.libelle_categorie == "":
                            return jsonify({
                            "Success": False,
                            "Message": "Champs vides !"
                        })
                        else:
                        # rqt = Categorie.query.filter(Categorie.libelle_categorie == categorie.libelle_categorie).all()
                        # if rqt:
                        #     return jsonify({
                        #         "Success": False,
                        #         "Message": "La categorie existe déjà !"
                        #     })
                        # else:
                            categorie.updateCategorie()

                    return jsonify({
                        'Success': True,
                        'Categorie': categorie.formatCategorie(),
                        'Nombre categorie': len(categories)
                        })
                except:
                    abort(400)
        except:
            # Method is wrong
            abort(405)
        finally:
            db.session.close()

    except:
        abort(404)

# =========================================
#
#   DATA Categorie(id) (show)
#
# =========================================


def show_a_category_id(categorieId):

    try:
        try:
            # show a categorie
            if request.method == "GET":
                try:
                    categories = Categorie.query.all()
                    categorie = Categorie.query.get(categorieId)

                    if categorie is None:
                        return jsonify({
                            "Success": False,
                            "Message": "La categorie n'existe pas !"
                        })
                    else:
                        return jsonify({
                            'Success': True,
                            'Categorie': categorie.formatCategorie(),
                            'Nombre categorie': len(categories)
                        })
                except:
                    abort(400)
        except:
            abort(405)
        finally:
            db.session.close()
    except:
        abort(404)

# =========================================
#
#   DATA Livre(id) (show)
#   Tips : For the show use another way than the format to make the data a json
#   also practice to make join in sqlalchemy
#
# =========================================


def show_a_book_id(livreId):

    try:
        try:
            if request.method == "GET":
                try:
                    livres = Livre.query.all()
                    livre = Livre.query.get(livreId)

                    # None => id not found
                    if livre is None:
                        return jsonify({
                            "Success": False,
                            "Message": "Le livre n'existe pas !"
                        })
                    else:
                        # A join to find the categorie name of a book
                        les_livres = db.session.query(
                            Categorie, Livre).join(Livre).filter(
                            Livre.id == livreId).all()

                        # Empty dictionnary
                        dict_livre = []
                        # Transform all data find in obj and transform it to a json to
                        # put it in a dictionnary
                        for one in les_livres:
                            one_obj = {}
                            one_obj['id'] = one.Livre.id
                            one_obj['isbn'] = one.Livre.isbn
                            one_obj['Titre'] = one.Livre.titre
                            one_obj['Date publication'] = one.Livre.date_publication
                            one_obj['Auteur'] = one.Livre.auteur
                            one_obj['Editeur'] = one.Livre.editeur
                            one_obj['id categorie'] = one.Categorie.id
                            one_obj['Categorie'] = one.Categorie.libelle_categorie
                            dict_livre.append(one_obj)

                        return jsonify({
                            'Success': True,
                            'Livre': dict_livre,
                            'Nombre Livre': len(livres)
                        })
                except:
                    abort(400)
        except:
            abort(405)
    except:
        abort(404)
# =========================================
#
#   DATA Livre (show book by category)
#
# =========================================


def show_book_by_category_id(categorieId):

    try:
        try:
            if request.method == "GET":
                try:
                    livres = Livre.query.all()
                    livre_cat = Livre.query.filter_by(categorie_id=categorieId).all()
                    livre_format = [livre.formatLivre() for livre in livre_cat]

                    if categorieId is None:
                        return jsonify({
                            'Success': False,
                            "Message": "La categorie n'existe pas !"
                        })
                    elif livre_format is None:
                        return jsonify({
                            'Success': True,
                            "Message": "Aucun livre dans cette categorie !"
                        })
                    else:
                        return jsonify({
                            'Success': True,
                            'Livre': livre_format,
                            'Nombre Livre': len(livres)
                        })
                except:
                    abort(400)
        except:
            abort(405)
    except:
        abort(404)
