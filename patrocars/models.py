from sqlmodel import SQLModel, Field
from typing import Optional
from typing import Optional

class Montadora(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  nome: str
  pais: str
  ano_fundacao: int

class Modelo(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  montadora_id: str
  nome: str
  valor_referencia: int
  motorizacao: int
  turbo: bool
  automatico: bool
  
class Veiculo(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  modelo_id: int
  cor: str
  ano_fabricacao: int
  ano_modelo: int
  valor: int
  placa: str
  vendido: bool