from pydantic import BaseModel

class ClienteSchema(BaseModel):
    """ Define como o cliente a ser inserido deve ser representado
    """

    nome: str = "allison tomé da silva"
    cpf: str = "11122233300"
    telefone: str = "81955556666"
    nome_corretor: str ="escritório"