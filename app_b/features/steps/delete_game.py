import requests
import time
from behave import given, when, then, step

@then(u'faca um post excluindo o jogo')
def step_impl(context):
    time.sleep(30)
    context.body = requests.delete("http://127.0.0.1:5000/game/" + str(context.body['id']))

@then(u'deve retornar um body com a mensagem "{message}"')
def step_impl(context, message):
    assert context.body.json()["message"] == message, \
        'Erro de assert {} != {}'.format(message, context.body.json()["message"])