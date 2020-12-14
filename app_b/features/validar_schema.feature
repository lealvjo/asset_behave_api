#language: pt

@teste
Funcionalidade: Os retornos devem estar de acordo com o schema

  Contexto:
    Dado faca get de um jogo no endpoint "/game/"
    E deve me retornar o status code "200"

  Cenario: Validar schema do json do jogo retornado
    Entao deve ser retornado de acordo com o schema "data_order.json"
