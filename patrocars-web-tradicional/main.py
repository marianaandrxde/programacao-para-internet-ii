from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlmodel import SQLModel
from persistence import db
from models import Montadora, Modelo, Veiculo
from persistence.montadora_repository import MontadoraRepository
from persistence.modelo_repository import ModeloRepository
from view_models import InputMontadora, InputModelo, InputVeiculo

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount("/images", StaticFiles(directory="images"), name="images")


templates = Jinja2Templates(directory='templates')

SQLModel.metadata.create_all(db.engine)

montadoras: list[Montadora] = []
modelos: list[Modelo] = []
veiculos: list[Veiculo] = []

montadora_repository = MontadoraRepository()
modelo_repository = ModeloRepository()


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(db.engine)

# Montadoras
    
@app.get('/montadoras_list')
def montadora_list(request: Request):
  montadoras = montadora_repository.get_all()


  return templates.TemplateResponse(
    request=request, 
    name='/montadora/montadora_list.html', 
    context={'montadoras': montadoras}
  )


@app.get('/montadoras_form')
def montadora_form(request: Request):
  return templates.TemplateResponse(request, '/montadora/montadora_form.html')


@app.get('/montadora_edit/{montadora_id}')
async def montadora_form(request: Request, montadora_id: int):
    montadora = montadora_repository.get_by_id(montadora_id)  
    if not montadora:
        return RedirectResponse('/montadoras_list', status_code=404)  
    return templates.TemplateResponse("/montadora/montadora_edit.html", {"request": request, "montadora": montadora})


@app.get('/montadora_delete/{montadora_id}')
async def montadora_form(request: Request, montadora_id: int):
    montadora = montadora_repository.get_by_id(montadora_id) 
    if not montadora:
        return RedirectResponse('/montadoras_list', status_code=404)
    return templates.TemplateResponse("/montadora/montadora_delete.html", {"request": request, "montadora": montadora})


@app.post('/montadora_save')
def montadora_save(request: Request, input: Annotated[InputMontadora, Form()]):
  montadora = Montadora(nome=input.nome, pais=input.pais, ano_fundacao=input.ano)
  montadora_repository.save(montadora)
  return RedirectResponse('/montadoras_list', status_code=303)


@app.post('/montadora_edit/{montadora_id}')
async def montadora_edit(montadora_id: int, request: Request, input: Annotated[InputMontadora, Form()]):
    montadora = Montadora(nome=input.nome, pais=input.pais, ano_fundacao=input.ano)
    montadora_repository.update(montadora_id, montadora)
    return RedirectResponse('/montadoras_list', status_code=303)


@app.post('/montadora_delete/{montadora_id}')
async def montadora_delete(montadora_id: int, request: Request, input: Annotated[InputMontadora, Form()]):
    montadora = Montadora(nome=input.nome, pais=input.pais, ano_fundacao=input.ano)
    montadora_repository.delete(montadora_id, montadora)  
    return RedirectResponse('/montadoras_list', status_code=303)


# Modelos

@app.get('/modelos_list')
def modelo_list(request: Request):
  modelos = modelo_repository.get_all()


  return templates.TemplateResponse(
    request=request, 
    name='/modelo/modelo_list.html', 
    context={'modelos': modelos}
  )


@app.get('/modelos_form')
def modelo_form(request: Request):
  montadoras = montadora_repository.get_all() 
  return templates.TemplateResponse(
        request=request, 
        name='/modelo/modelo_form.html', 
        context={'montadoras': montadoras}
    )

@app.get('/modelo_edit/{modelo_id}')
async def modelo_form(request: Request, modelo_id: int):
    modelo = modelo_repository.get_by_id(modelo_id)  
    if not modelo:
        return RedirectResponse('/modelo_list', status_code=404)  
    return templates.TemplateResponse("/modelo/modelo_edit.html", {"request": request, "modelo": modelo})


@app.get('/modelo_delete/{modelo_id}')
async def modelo_form(request: Request, modelo_id: int):
    modelo = modelo_repository.get_by_id(modelo_id) 
    if not modelo:
        return RedirectResponse('/modelos_list', status_code=404)
    return templates.TemplateResponse("/modelo/modelo_delete.html", {"request": request, "modelo": modelo})


@app.post('/modelo_save')
def modelo_save(request: Request, input: Annotated[InputModelo, Form()]):
  modelo = Modelo(montadora_id = input.montadora_id, nome=input.nome, valor_referencia=input.valor_referencia, motorizacao=input.motorizacao, turbo=input.turbo, automatico=input.automatico)
  modelo_repository.save(modelo)
  return RedirectResponse('/modelos_list', status_code=303)


@app.post('/modelo_edit/{modelo_id}')
async def modelo_edit(modelo_id: int, request: Request, input: Annotated[InputModelo, Form()]):
    modelo = Modelo( montadora_id=input.montadora_id, nome=input.nome, valor_referencia=input.valor_referencia, motorizacao=input.motorizacao, turbo=input.turbo, automatico=input.automatico)
    modelo_repository.update(modelo_id, modelo)
    return RedirectResponse('/modelos_list', status_code=303)

@app.post('/modelo_delete/{modelo_id}')
async def modelo_delete(modelo_id: int, request: Request, input: Annotated[InputModelo, Form()]):
    modelo = Modelo(montadora_id = input.montadora_id, nome=input.nome, valor_referencia=input.valor_referencia, motorizacao=input.motorizacao, turbo=input.turbo, automatico=input.automatico)
    modelo_repository.delete(modelo_id, modelo)  
    return RedirectResponse('/modelos_list', status_code=303)