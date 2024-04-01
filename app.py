from flask_openapi3 import OpenAPI, Info, Tag
from flask import jsonify, redirect
from sqlalchemy.exc import IntegrityError

from model import *
from schemas import *

info = Info
app = OpenAPI(__name__)


cliente_tag = Tag(name="cliente", description="adição, remoção e edição do cliente na base da dados")

@app.get('/')
def documentacao():
    return redirect('/openapi')

@app.post("/cliente", tags=[cliente_tag])
def cadastra_cliente(form: ClienteSchema):
    cliente = Cliente(
        nome = form.nome,
        cpf = form.cpf,
        telefone = form.telefone,
        nome_corretor = form.nome_corretor
    )
    
    try:
        session.add(cliente)
        session.commit()

        return { "mensage": "cliente cadastrado"}, 200
    
    except IntegrityError as e:

        return { "mensage" : "cliente já cadastrado" }


@app.get("/clientes", tags=[cliente_tag],
         responses= {"200": ClienteSchema })
def clientes():

    clientes = session.query(Cliente).all()

    if not clientes:
        return { "clientes": [] }, 200
    else:
        return clientes
    


if __name__ == "__main__":
    app.run()