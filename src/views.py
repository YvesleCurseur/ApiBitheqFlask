from flask import Blueprint

# Import def alias controllers from src directory
from src.controllers import index, show_and_add_book, show_and_add_category, show_a_book_id, show_a_category_id, update_and_delete_book_id, update_and_delete_category_id, show_book_by_category_id

# Fonction To make a "Route Type"
chemin = Blueprint('chemin', __name__)

chemin.route('/', methods=['GET'])(index)

chemin.route('/livre/<int:livreId>', methods=['GET'])(show_a_book_id)
chemin.route('/categorie/<int:categorieId>', methods=['GET'])(show_a_category_id)

chemin.route('/livre', methods=['GET', 'POST'])(show_and_add_book)
chemin.route('/categorie', methods=['GET', 'POST'])(show_and_add_category)

chemin.route('/livre/<int:livreId>', methods=['PATCH', 'DELETE'])(update_and_delete_book_id)
chemin.route('/categorie/<int:categorieId>', methods=['PATCH', 'DELETE'])(update_and_delete_category_id)

chemin.route('/livre/categorie/<int:categorieId>', methods=['GET'])(show_book_by_category_id)

