import requests
from behave import given, when
from game.create_game import CreateGame

@given(u'que altere o preco do jogo enviado')
def step_impl(context):
    context.obj_game = CreateGame()

@when(u'eu alterar e enviar no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    context.body = requests.put(context.stage + endpoint + str(context.body['id']),
                                json=context.obj_game.get_body_game())

