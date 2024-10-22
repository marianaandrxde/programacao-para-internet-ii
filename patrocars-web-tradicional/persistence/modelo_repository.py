from sqlmodel import Session, select
from models import Modelo
from persistence import db

class ModeloRepository():

  def __init__(self):
    self.session = Session(db.engine)

  def get_all(self):
    sttm = select(Modelo)
    modelos = self.session.exec(sttm).all()
    return modelos
  
  def get_by_id(self, modelo_id: int) -> Modelo:
    return self.session.get(Modelo, modelo_id)

  
  def save(self, modelo: Modelo):
    self.session.add(modelo)
    self.session.commit()
    self.session.refresh(modelo)
    return modelo
  

  def update(self, modelo_id: int, updated_modelo: Modelo):
        existing_modelo = self.session.get(Modelo, modelo_id)
        if existing_modelo:
            existing_modelo.montadora_id = updated_modelo.montadora_id
            existing_modelo.nome = updated_modelo.nome
            existing_modelo.valor_referencia = updated_modelo.valor_referencia
            existing_modelo.motorizacao = updated_modelo.motorizacao
            existing_modelo.turbo = updated_modelo.turbo
            existing_modelo.automatico = updated_modelo.automatico
            
            self.session.commit()
            self.session.refresh(existing_modelo)
            return existing_modelo
        else:
            raise ValueError(f"Modelo com ID {modelo_id} não encontrado.")
        
  def delete(self, modelo_id: int, modelo: Modelo):
        modelo = self.session.get(Modelo, modelo_id)
        if not modelo:
           raise ValueError(f"Modelo com ID {modelo_id} não encontrado.")
        else:
          self.session.delete(modelo)
          self.session.commit()
          return {"ok": True}

