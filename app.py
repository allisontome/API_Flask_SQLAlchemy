from flask_openapi3 import OpenAPI
from flask import jsonify

from model import Session, Cliente, Corretor

app = OpenAPI(__name__)

@app.get("/cliente")
def cliente():
    return jsonify({
        "nome": "allison"
    })


if __name__ == "__main__":
    app.run()