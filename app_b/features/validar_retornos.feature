#language: pt

@teste2
Funcionalidade: Validar se o retorno do jogo e igual que foi enviado

    Contexto:
        Dado faca post de um novo jogo
        E o atributo "page_indx" possuir o valor "11"
        E o atributo "name" possuir o valor "CyberPunk 2077"
        E o atributo "price" possuir o valor "R$ 200,00"
        E o atributo "game_link" possuir o valor "http://teste"
        E o atributo "game_pht" possuir o valor "http://teste"
        Quando eu enviar no endpoint "/game"
        Entao deve me retornar o status code "201"
        E deve me retornar um body do jogo adicionado

    Cenario: Validar os campos do body do jogo
        Dado faca get do jogo no endpoint "/game/"
        Entao deve me retornar o status code "200"
        E o campo "page_indx" deve ser igual ao valor "11"
        E o campo "name" deve ser igual ao valor "CyberPunk 2077"
        E o campo "price" deve ser igual ao valor "R$ 200,00"
        E o campo "game_link" deve ser igual ao valor "http://teste"
        E o campo "game_pht" deve ser igual ao valor "http://teste"
