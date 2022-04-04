from flask import Blueprint

from controllers.bibliotheque_controller import index, storeLivre, storeCategorie, showLivre, showCategorie, showCategorieId, showLivreId, editCategorie, editLivre

bibliotheque_path = Blueprint('bibliotheque_path', __name__)

bibliotheque_path.route('/', methods=['GET'])(index)

bibliotheque_path.route('/livre', methods=['GET'])(showLivre)
bibliotheque_path.route('/categorie', methods=['GET'])(showCategorie)

bibliotheque_path.route('/livre/<int:livreId>', methods=['GET'])(showLivreId)
bibliotheque_path.route('/categorie/<int:categorieId>', methods=['GET'])(showCategorieId)

bibliotheque_path.route('/create/livre', methods=['POST'])(storeLivre)
bibliotheque_path.route('/create/categorie', methods=['POST'])(storeCategorie)

bibliotheque_path.route('edit/livre/<int:livreId>', methods=['PATCH'])(editLivre)
bibliotheque_path.route('/edit/categorie/<int:categorieId>', methods=['PATCH'])(editCategorie)

# bibliotheque_path.route('/<int:user_id>', methods=['DELETE'])(delete)