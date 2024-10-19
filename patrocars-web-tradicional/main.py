from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from sqlmodel import SQLModel


from models import Montadora
from persistence.utils import get_engine
from persistence.montadora_repository import MontadoraRepository
from view_models import InputMontadora

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount("/images", StaticFiles(directory="images"), name="images")


templates = Jinja2Templates(directory='templates')

# Montadora
SQLModel.metadata.create_all(get_engine())

montadoras: list[Montadora] = []

repository = MontadoraRepository()

@app.get('/montadoras_list')
def montadora_list(request: Request):
  montadoras = repository.get_all()


  return templates.TemplateResponse(
    request=request, 
    name='montadora_list.html', 
    context={'montadoras': montadoras}
  )


@app.get('/montadoras_form')
def montadora_form(request: Request):
  return templates.TemplateResponse(request, 'montadora_form.html')


@app.get('/montadora_edit/{montadora_id}')
async def montadora_form(request: Request, montadora_id: int):
    montadora = repository.get_by_id(montadora_id)  # Obtém a montadora pelo ID
    if not montadora:
        return RedirectResponse('/montadoras_list', status_code=404)  # Ou outra lógica de erro
    return templates.TemplateResponse("montadora_edit.html", {"request": request, "montadora": montadora})


@app.get('/montadora_delete/{montadora_id}')
async def montadora_form(request: Request, montadora_id: int):
    montadora = repository.get_by_id(montadora_id)  # Obtém a montadora pelo ID
    if not montadora:
        return RedirectResponse('/montadoras_list', status_code=404)  # Ou outra lógica de erro
    return templates.TemplateResponse("montadora_delete.html", {"request": request, "montadora": montadora})


@app.post('/montadora_save')
def montadora_save(request: Request, input: Annotated[InputMontadora, Form()]):
  montadora = Montadora(nome=input.nome, pais=input.pais, ano_fundacao=input.ano)
  repository.save(montadora)
  return RedirectResponse('/montadoras_list', status_code=303)


@app.post('/montadora_edit/{montadora_id}')
async def montadora_edit(montadora_id: int, request: Request, input: Annotated[InputMontadora, Form()]):
    montadora = Montadora(nome=input.nome, pais=input.pais, ano_fundacao=input.ano)
    repository.update(montadora_id, montadora)
    return RedirectResponse('/montadoras_list', status_code=303)


@app.post('/montadora_delete/{montadora_id}')
async def montadora_delete(montadora_id: int, request: Request, input: Annotated[InputMontadora, Form()]):
    montadora = Montadora(nome=input.nome, pais=input.pais, ano_fundacao=input.ano)
    repository.delete(montadora_id, montadora)  
    return RedirectResponse('/montadoras_list', status_code=303)