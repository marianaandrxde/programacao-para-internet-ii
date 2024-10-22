from sqlmodel import Session, select
from models import Montadora
from persistence import db

class MontadoraRepository():

  def __init__(self):
    self.session = Session(db.engine)

  def get_all(self):
    sttm = select(Montadora)
    montadoras = self.session.exec(sttm).all()
    return montadoras
  
  def get_by_id(self, montadora_id: int) -> Montadora:
    return self.session.get(Montadora, montadora_id)

  
  def save(self, montadora: Montadora):
    self.session.add(montadora)
    self.session.commit()
    self.session.refresh(montadora)
    return montadora
  

  def update(self, montadora_id: int, updated_montadora: Montadora):
        existing_montadora = self.session.get(Montadora, montadora_id)
        if existing_montadora:
            existing_montadora.nome = updated_montadora.nome
            existing_montadora.pais = updated_montadora.pais
            existing_montadora.ano_fundacao = updated_montadora.ano_fundacao
            
            self.session.commit()
            self.session.refresh(existing_montadora)
            return existing_montadora
        else:
            raise ValueError(f"Montadora com ID {montadora_id} não encontrada.")
        
  def delete(self, montadora_id: int, montadora: Montadora):
        montadora = self.session.get(Montadora, montadora_id)
        if not montadora:
           raise ValueError(f"Montadora com ID {montadora_id} não encontrado.")
        else:
          self.session.delete(montadora)
          self.session.commit()
          return {"ok": True}

