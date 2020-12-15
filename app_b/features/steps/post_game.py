import requests
from behave import given

@given(u'faca post de um novo jogo no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    myobj = {
    "page_indx": 11,
    "name": "JOGO TESTE",
    "price": "R$ 50,00",
    "game_link": "teste",
    "game_pht": "teste"
}
    context.body = requests.post(context.stage + endpoint, json=myobj)

@given(u'deve me retornar um body do jogo adicionado')
def step_impl(context):
    context.body = context.body.json()