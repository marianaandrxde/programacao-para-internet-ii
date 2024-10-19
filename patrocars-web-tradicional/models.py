from sqlmodel import SQLModel, Field
from typing import Optional
from typing import Optional

class Montadora(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  nome: str
  pais: str
  ano_fundacao: int