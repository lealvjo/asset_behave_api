#language: pt

@teste1
Funcionalidade: Os retornos devem estar de acordo com o schema

  Contexto:
    Dado faca get de um jogo no endpoint "/game/"

  Cenario: Validar schema json do jogo retornado
    Entao deve me retornar o status code "200"
    E deve ser retornado de acordo com o schema "data_order.json"
