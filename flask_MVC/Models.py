from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categorie (db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50), nullable=False)  
    livres = db.relationship('Livre',  backref='categories', lazy=True)

# =========================================
#
# Make the Constructor
#
# =========================================

    # def __init__(self, libelle_categorie):
    #     """initialize with name."""
    #     self.libelle_categorie = libelle_categorie 

# =========================================
#
# Method insert, delete, update & get data 
#
# =========================================

    def insertCategorie(self):
        db.session.add(self)
        db.session.commit()

    def deleteCategorie(self):
        db.session.delete(self)
        db.session.commit()
    
    def updateCategorie(self):
        db.session.commit()

    def formatCategorie(self):
        return {
            'id': self.id,
            'Libelle Categorie': self.libelle_categorie
        }

# =========================================
#
# Create the Model
#
# =========================================

class Livre (db.Model):
    __tablename__='livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(15), nullable=False)   
    titre = db.Column(db.String(50), nullable=False)
    date_publication = db.Column(db.DateTime, nullable=False)
    auteur = db.Column(db.String(50), nullable=False)
    editeur = db.Column(db.String(50), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

# =========================================
#
# Make the Constructor
#
# =========================================

    # def __init__(self, isbn, titre, date_publication, auteur, editeur, categorie_id):
    #     """initialize with name."""
    #     self.isbn = isbn
    #     self.titre = titre
    #     self.date_publication = date_publication
    #     self.auteur = auteur
    #     self.editeur = editeur
    #     self.categorie_id = categorie_id

# =========================================
#
# Method insert, delete, update & get data 
#
# =========================================
 
def insertLivre(s):
    db.session.add(s)
    db.session.commit()

def deleteLivre(s):
    db.session.delete(s)
    db.session.commit()

def updateLivre(s):
    db.session.commit()

# =========================================
#
# Show data in json format 
#
# =========================================

    def formatLivre(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'Titre' : self.titre,
            'Date publication': self.date_publication,
            'Auteur': self.auteur,
            'Editeur': self.editeur,
            'Categorie': self.categorie_id
        }

