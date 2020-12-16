import requests
from behave import given, then

@given(u'faca get do jogo no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    context.body = requests.get(context.stage + endpoint + str(context.body.json()['id']))

@then(u'deve me retornar o status code "{status_code}"')
def step_impl(context, status_code):
    assert context.body.status_code == int(status_code),  \
        'Erro de assert {} != {}'.format(status_code, context.body.status_code)

@then(u'o campo "{field}" deve ser igual ao valor "{value}"')
def step_impl(context, field, value):
    assert context.body.json()[field] == value, \
        'Erro de assert {} != {}'.format(context.body.json()[field], value)