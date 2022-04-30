from flask import Blueprint
# Import def alias controllers from Flask_MVC directory
from flask_mvc.controllers import index, show_and_add_book, show_and_add_category, show_a_book_id, show_a_category_id, update_and_delete_book_id, update_and_delete_category_id, show_book_by_category_id

# Fonction To make a "Route Type"
the_path = Blueprint('the_path', __name__)

the_path.route('/',
               methods=['GET'])(index)

the_path.route('/livre/<int:livreId>',
               methods=['GET'])(show_a_book_id)
the_path.route('/categorie/<int:categorieId>',
               methods=['GET'])(show_a_category_id)

the_path.route('/livre',
               methods=['GET', 'POST'])(show_and_add_book)
the_path.route('/categorie',
               methods=['GET', 'POST'])(show_and_add_category)


the_path.route('/livre/<int:livreId>',
               methods=['PATCH', 'DELETE'])(update_and_delete_book_id)
the_path.route('/categorie/<int:categorieId>',
               methods=['PATCH', 'DELETE'])(update_and_delete_category_id)

the_path.route('/livre/categorie/<int:categorieId>',
               methods=['GET'])(show_book_by_category_id)

the_path.errorhandler(400)
the_path.errorhandler(405)
the_path.errorhandler(404)
