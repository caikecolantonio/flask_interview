from flask import Flask, jsonify
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

config_db(app)
config_ma(app)

Migrate(app, app.db)

from .usuarios import bp_usuarios
app.register_blueprint(bp_usuarios)


@app.route('/get', methods = ['GET'])
def get_teste():
    return jsonify({'Hello':'World'})

if __name__ == "__main__":
    app.run(debug=True)