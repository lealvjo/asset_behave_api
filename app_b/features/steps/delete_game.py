import requests
import time
from behave import then, When

@when(u'faco um post excluindo o jogo no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    time.sleep(30)
    context.body = requests.delete(context.stage + endpoint + str(context.body.json()['id']))

@then(u'deve retornar um body com a mensagem "{message}"')
def step_impl(context, message):
    assert context.body.json()["message"] == message, \
        'Erro de assert {} != {}'.format(message, context.body.json()["message"])