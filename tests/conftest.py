import pytest 
from flask import Flask

@pytest.fixture(scope="module")
def app():
    "Instancia do app main"
    app = Flask(__name__)

    return app