from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect, request
from sqlalchemy.exc import IntegrityError

from model import *
from schemas import *


import logging

logging.basicConfig(level=logging.DEBUG)

info = Info
app = OpenAPI(__name__)
CORS(app)


cliente_tag = Tag(name="cliente", description="adição, remoção e edição do cliente na base da dados")
corretor_tag = Tag(name="corretor", description="adição, consulta e exclusão de dados do corretor da base de dados")
documentacao_tag = Tag(name="documentação", description="Consulta documentação da API")


@app.get('/', tags=[documentacao_tag])
def documentacao():
    """ Documentação da API
    """
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
    try:
        session = Session()
        cliente = session.query(Cliente).filter(Cliente.cpf == query.cpf).first()
        print(cliente.cpf)
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
def atualiza_cliente(form: EditaClienteSchema):
    """ Atualiza informações do cliente (Apenas nome, telefone e corretor)
    """
    session = Session()
    cliente = session.query(Cliente).filter(Cliente.id == form.id).first()

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


@app.delete("/cliente", tags=[cliente_tag], 
            responses= {
                "200": ClienteViewSchema,
                "400": ErrorSchema,
                "404": ErrorSchema
            })
def deletar_cliente(query: DeletaClienteSchema):

    """ Deleta o cliente do banco de dados
    """
    session = Session()
    cliente = session.query(Cliente).filter(Cliente.id == query.id).first()

    if not cliente:
        return {"message": "cliente não encontrado"}, 404
    
    try:
        session.delete(cliente)
        session.commit()
        return {
            "message": "Cliente deletado",
            "cliente": apresenta_cliente(cliente)
        }, 200
    
    except Exception as e:
        return {"message": "Erro ao deletar cliente"}, 400
    finally:
        session.close()


@app.get("/clientes", tags=[cliente_tag], 
         responses= {
             "200": ListaClienteSchema,
             "404": ErrorSchema,
             "400": ErrorSchema
         })
def consultar_todos_clientes():
    """ Retorna todos clientes cadastrados no banco
    """
    try:
        session = Session()
        clientes_response = session.query(Cliente).all()
    except Exception as e:
        return {"message": "erro ao consultar clientes"}, 400
    finally:
        session.close()

    if not clientes_response:
        return {"clientes": []}, 200
    else:
        return {"clientes": lista_clientes(clientes_response)}



@app.post("/corretor", tags=[corretor_tag])
def cadastra_corretor(form: CorretorSchema):
    """ Adiciona corretor a base de dados
    """
    corretor = Corretor(
        nome_corretor = form.nome_corretor,
        cpf = form.cpf,
        telefone = form.telefone
    )
    try:
        session = Session();
        session.add(corretor)
        session.commit()
        return {"message": "corretor cadastrado"}
    except Exception as e:
        return {"message": "Erro ao cadastrar corretor"}