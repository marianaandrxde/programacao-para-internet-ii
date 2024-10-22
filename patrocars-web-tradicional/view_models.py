from pydantic import BaseModel

class InputMontadora(BaseModel):
  nome: str
  pais: str
  ano: int

class InputModelo(BaseModel):
  montadora_id: str
  nome: str
  valor_referencia: int
  motorizacao: int
  turbo: bool
  automatico: bool

class InputVeiculo(BaseModel):
  modelo_id: int
  cor: str
  ano_fabricacao: int
  ano_modelo: int
  valor: int
  placa: str
  vendido: bool