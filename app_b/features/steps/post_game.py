import requests
from behave import given, when, then
from pojo.game import Game


@given(u'faca post de um novo jogo')
def step_impl(context):
    context.obj_game = Game()


@given(u'o atributo "{field}" possuir o valor "{value}"')
def step_impl(context, field, value):
    context.obj_game.set_field_game(field, value)


@when(u'eu enviar no endpoint "{endpoint}"')
def step_impl(context, endpoint):
    context.body = requests.post(context.stage + endpoint, json=context.obj_game.get_body_game())
