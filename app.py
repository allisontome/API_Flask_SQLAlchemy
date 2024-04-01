from flask_openapi3 import OpenAPI
from flask import jsonify, redirect
from sqlalchemy.exc import IntegrityError

from model import *

app = OpenAPI(__name__)

@app.get('/')
def documentacao():
    return redirect('/openapi')   


if __name__ == "__main__":
    app.run()