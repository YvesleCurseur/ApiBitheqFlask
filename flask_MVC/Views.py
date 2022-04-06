from flask import Blueprint
# Import def alias controllers from Flask_MVC directory
from flask_MVC.Controllers import index, show_and_add_livre, show_and_add_categorie, delete_livre, delete_categorie
# storeLivre, storeCategorie, showCategorie, showLivrePerCategorieId, showCategorieId, showLivreId, editCategorie, editLivre, 

# Fonction To make a "Route Type"
the_path = Blueprint('the_path', __name__)

the_path.route('/', methods=['GET'])(index)

the_path.route('/livre', methods=['GET', 'POST'])(show_and_add_livre)
the_path.route('/categorie', methods=['GET', 'POST'])(show_and_add_categorie)

# the_path.route('/categorie/<int:categorieId>/livre', methods=['GET'])(showLivrePerCategorieId)
# the_path.route('/categorie', methods=['GET'])(showCategorie)

# the_path.route('/livre/<int:livreId>', methods=['GET'])(showLivreId)
# the_path.route('/categorie/<int:categorieId>', methods=['GET'])(showCategorieId)

# the_path.route('/livre', methods=['POST'])(storeLivre)
# the_path.route('/categorie', methods=['POST'])(storeCategorie)

# the_path.route('/edit/livre/<int:livreId>', methods=['PATCH'])(editLivre)
# the_path.route('/edit/categorie/<int:categorieId>', methods=['PATCH'])(editCategorie)

the_path.route('livre/<int:livreId>', methods=['DELETE'])(delete_livre)
the_path.route('categorie/<int:categorieId>', methods=['DELETE'])(delete_categorie)