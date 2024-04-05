from pydantic import BaseModel, Field
from model.corretor import Corretor
from typing import Optional

class CorretorSchema(BaseModel):
    """ Apresenta como um corretor deve ser inserido no banco
    """
    nome_corretor: str = "escritorio"
    cpf: str = "00011122255"
    telefone: Optional[str] = "81998586958"
