# Patrocars Web Anos 2000

Este projeto é uma aplicação web desenvolvida utilizando FastAPI (Python), SQLModel e Jinja. 
O objetivo principal da aplicação é realizar operações de CRUD (Create, Read, Update, Delete) 
para gerenciar uma estrutura simples de montadoras, modelos e veículos.

### Estrutura do Sistema
- Montadora: Representa as empresas que fabricam veículos.
- Modelo: Cada montadora possui um ou mais modelos de veículos.
- Veículo: Cada veículo é associado a um modelo específico.

### Funcionalidades
- Montadoras: Possível cadastrar, listar, editar e excluir montadoras.
- Modelos: Cada modelo está associado a uma montadora. É possível gerenciar modelos da mesma forma.
- Veículos: Cada veículo pertence a um modelo, e você pode gerenciar as informações de veículos da mesma maneira.
### Tecnologias Utilizadas
- FastAPI: Framework de desenvolvimento web em Python, focado em alta performance e simplicidade.
- SQLModel: Biblioteca de ORM que combina o poder do SQLAlchemy com a facilidade de uso do Pydantic.
- Jinja: Template engine usada para renderizar páginas HTML dinâmicas.
### Como Executar
Acesse em: 
  
        https://patrocars-kahy.onrender.com
  



Ou clone o repositório.
- Instale as dependências listadas no requirements.txt.
- Seguindo o modelo do .env.example, adicione a URL do banco de dados. Sugiro a utilização de um serviço de banco de dados online, a fim de facilitar a realização do teste.
- Execute o servidor utilizando o Uvicorn com o comando:
  
       uvicorn main:app --reload --port 8000
  
A aplicação estará disponível em http://127.0.0.1:8000.
