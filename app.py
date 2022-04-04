from flask import Flask
from flask_migrate import Migrate

# Take data and path  
from models.bibliotheque import db
from routes.bibliotheque_path import bibliotheque_path

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(bibliotheque_path, url_prefix='/bibliotheque')

if __name__ == '__main__':
    app.debug = True
    app.run()