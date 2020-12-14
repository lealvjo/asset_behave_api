import requests
from behave import given, when, then, step

@given(u'faca post de um novo jogo no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    myobj = {
    "page_indx": 11,
    "name": "JOGO TESTE",
    "price": "R$ 50,00",
    "game_link": "teste",
    "game_pht": "teste"
}
    context.body = requests.post(endpoint, json=myobj)

@given(u'deve me retornar o status code "{status_code}"')
def step_impl(context, status_code):
    assert context.body.status_code == int(status_code),  \
        'Erro de assert {} != {}'.format(status_code, context.body.status_code)

@given(u'deve me retornar um body do jogo adicionado')
def step_impl(context):
    context.body = context.body.json()