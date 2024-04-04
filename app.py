from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from sqlalchemy.exc import IntegrityError

from model import *
from schemas import *


import logging

logging.basicConfig(level=logging.DEBUG)

info = Info
app = OpenAPI(__name__)


cliente_tag = Tag(name="cliente", description="adição, remoção e edição do cliente na base da dados")

@app.get('/')
def documentacao():
    return redirect('/openapi')

@app.post("/cliente", tags=[cliente_tag],
          responses={
              "200": ClienteViewSchema,
              "400": ErrorSchema,
              "409": ErrorSchema
          })
def cadastra_cliente(form: ClienteSchema):
    """ Adiciona novo cliente à base de dados
    """
    cliente = Cliente(
        nome = form.nome,
        cpf = form.cpf,
        telefone = form.telefone,
        nome_corretor = form.nome_corretor
    )
    try:
        session = Session()
        session.add(cliente)
        session.commit()
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        return { "message" : "cliente já cadastrado" }, 409
    
    except Exception as e:
        return {"message": "Erro ao adicionar o cliente."}, 400
    finally:
        session.close()


@app.get("/cliente", tags=[cliente_tag],
         responses= {
             "200": ClienteViewSchema, 
             "400": ErrorSchema, 
             "404": ErrorSchema })
def consulta_cliente(query: ConsultaClienteSchema):
    """ Consulta cliente individual por CPF
    """
    cpf = query.cpf
    try:
        session = Session()
        cliente = session.query(Cliente).where(Cliente.cpf == cpf).first()
        if cliente:
            return apresenta_cliente(cliente), 200
        else:
            return {"message": "cliente não encontrado"}, 404
        
    except Exception as e:
        return {"message": "Erro ao procurar cliente"}, 400
    finally:
        session.close()



@app.put("/cliente", tags=[cliente_tag],
          responses={
              "200": ClienteViewSchema,
              "400": ErrorSchema,
              "404": ErrorSchema
          })
def atualiza_cliente(form: ClienteSchema):
    session = Session()
    cliente = session.query(Cliente).filter(Cliente.cpf == form.cpf).first()

    if not cliente:
        return {"message": "cliente não encontrado"}, 404
    
    try:
        cliente.nome = form.nome
        cliente.telefone = form.telefone
        cliente.nome_corretor = form.nome_corretor

        session.commit()
        return apresenta_cliente(cliente), 200
    
    except Exception as e:
        return {"message": "Erro ao atualizar cliente"}, 400
    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)