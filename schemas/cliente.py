from pydantic import BaseModel, Field
from model.cliente import Cliente
from typing import List, Optional

class ClienteSchema(BaseModel):
    """ Define como o cliente a ser inserido deve ser representado
    """
    
    nome: str = "allison tomé da silva"
    cpf: str = "11122233300"
    telefone: str = "81955556666"
    nome_corretor: str ="escritório"

class ClienteViewSchema(BaseModel):
    """ Define como o cliente será retornado
    """
    id: int = 1
    nome: str = "allison tome da silva"
    cpf: str = "111******00"
    telefone: Optional[str] = "819555666"
    nome_corretor: str = "escritório"

def format_cpf(cpf):
    return cpf[:3] + '*' * 5 + cpf[9:]

def apresenta_cliente(cliente):
    cpf_formatado = format_cpf(cliente.cpf)

    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "cpf": cpf_formatado,
        "telefone": cliente.telefone,
        "corretor": cliente.nome_corretor
    }

def lista_clientes(clientes: List[Cliente]):

    lista = []
    for cliente in clientes:
        lista.append(apresenta_cliente(cliente))
    
    return lista;
    

class ConsultaClienteSchema(BaseModel):
    """ Define o parâmetro da busca individual de clientes
    """
    cpf: str = Field("11122233300", description="CPF do Cliente")


class DeletaClienteSchema(BaseModel):
    """ Define o parametro para deletar cliente como o ID
    """
    id: int = Field(0, description="ID do cliente")

class EditaClienteSchema(BaseModel):
    """ Define os paramêtros a serem recebidos para edição do cliente
    """
    id: int = 1
    nome: str = "allison tome da silva"
    telefone: str = "819555666"
    nome_corretor: str = "escritório"
    

class ListaClienteSchema(BaseModel):
    """ Retorna a lista de clientes cadastrados
    """
    clientes: list[ClienteViewSchema]