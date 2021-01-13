import requests
from behave import given, when
from pojo.game import Game

@given(u'que altere o preco do jogo enviado')
def step_impl(context):
    context.obj_game = Game()

@when(u'eu alterar e enviar no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    context.body = requests.put(context.stage + endpoint + str(context.body.json()['id']),
                                json=context.obj_game.get_body_game())

