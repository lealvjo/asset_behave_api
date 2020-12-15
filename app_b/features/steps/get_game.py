import requests
from behave import given, then

@given(u'faca get de um jogo no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    context.body = requests.get(context.stage + endpoint + "10")

@then(u'deve me retornar o status code "{status_code}"')
def step_impl(context, status_code):
    assert context.body.status_code == int(status_code),  \
        'Erro de assert {} != {}'.format(status_code, context.body.status_code)
