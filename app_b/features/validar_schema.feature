#language: pt

@teste1
Funcionalidade: Os retornos devem estar de acordo com o schema

  Contexto:
    Dado faca post de um novo jogo
    E o atributo "page_indx" possuir o valor "11"
    E o atributo "name" possuir o valor "CyberPunk 2077"
    E o atributo "price" possuir o valor "R$ 200,00"
    E o atributo "game_link" possuir o valor "http://teste"
    E o atributo "game_pht" possuir o valor "http://teste"
    Quando eu enviar no endpoint "/game"
    Entao deve me retornar o status code "201"

  Cenario: Validar schema json do jogo retornado
    Dado faca get do jogo no endpoint "/game/"
    Entao deve me retornar o status code "200"
    E deve ser retornado de acordo com o schema "data_order.json"