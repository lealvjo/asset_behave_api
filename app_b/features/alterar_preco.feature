#language: pt

@teste1
Funcionalidade: Alterar o preço de um jogo enviado a loja

    Contexto:
      Dado faca post de um novo jogo
      E o atributo "page_indx" possuir o valor "11"
      E o atributo "name" possuir o valor "CyberPunk 2077"
      E o atributo "price" possuir o valor "R$ 200,00"
      E o atributo "game_link" possuir o valor "http://teste"
      E o atributo "game_pht" possuir o valor "http://teste"
      Quando eu enviar no endpoint "/game"
      Entao deve me retornar o status code "201"

    Cenario: Deve realizar alteracao do preco do jogo
      Dado que altere o preco do jogo enviado
      E o atributo "price" possuir o valor "R$ 300,00"
      Quando eu alterar e enviar no endpoint "/game/"
      Entao deve me retornar o status code "200"

    Esquema do Cenario: Deve realizar alteracao varias vezes
      Dado que altere o preco do jogo enviado
      E o atributo "price" possuir o valor "<price>"
      Quando eu alterar e enviar no endpoint "/game/"
      Entao deve me retornar o status code "200"

      Exemplos:  BlackFriday
          | price         |
          | R$ 100,00     |
          | R$ 200,00     |
          | R$ 300,00     |
          | R$ 400,00     |
          | R$ 500,00     |