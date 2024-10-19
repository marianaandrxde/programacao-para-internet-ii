from sqlmodel import Session, select
from .utils import get_engine
from models import Montadora

class MontadoraRepository():

  def __init__(self):
    self.session = Session(get_engine())

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
        # Buscando a montadora existente
        existing_montadora = self.session.get(Montadora, montadora_id)
        if existing_montadora:
            # Atualizando os campos desejados
            existing_montadora.nome = updated_montadora.nome
            existing_montadora.pais = updated_montadora.pais
            existing_montadora.ano_fundacao = updated_montadora.ano_fundacao
            
            # Comitando as alterações
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

