from sqlmodel import Session, select
from models import Veiculo
from persistence import db

class VeiculoRepository():

  def __init__(self):
    self.session = Session(db.engine)

  def get_all(self):
    sttm = select(Veiculo)
    veiculos = self.session.exec(sttm).all()
    print(veiculos)
    return veiculos
  
  def get_by_id(self, veiculo_id: int) -> Veiculo:
    return self.session.get(Veiculo, veiculo_id)

  
  def save(self, veiculo: Veiculo):
    self.session.add(veiculo)
    self.session.commit()
    self.session.refresh(veiculo)
    return veiculo


  def update(self, veiculo_id: int, updated_veiculo: Veiculo):
        existing_veiculo = self.session.get(Veiculo, veiculo_id)
        if existing_veiculo:
            existing_veiculo.modelo_id = updated_veiculo.modelo_id
            existing_veiculo.cor = updated_veiculo.cor
            existing_veiculo.ano_fabricacao = updated_veiculo.ano_fabricacao
            existing_veiculo.ano_modelo = updated_veiculo.ano_modelo
            existing_veiculo.valor = updated_veiculo.valor
            existing_veiculo.placa = updated_veiculo.placa
            existing_veiculo.vendido = updated_veiculo.vendido

            
            self.session.commit()
            self.session.refresh(existing_veiculo)
            return existing_veiculo
        else:
            raise ValueError(f"Veiculo com ID {veiculo_id} não encontrado.")
        
  def delete(self, veiculo_id: int, veiculo: Veiculo):
        veiculo = self.session.get(Veiculo, veiculo_id)
        if not veiculo:
           raise ValueError(f"Veículo com ID {veiculo_id} não encontrado.")
        else:
          self.session.delete(veiculo)
          self.session.commit()
          return {"ok": True}

