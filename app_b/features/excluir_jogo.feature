#language: pt

@teste
Funcionalidade: Excluindo um jogo

Cenario: Deve realizar a exclusao de jogos
    Dado faca post de um novo jogo no endpoint "/game"
    E deve me retornar o status code "201"
    E deve me retornar um body do jogo adicionado
    Entao faca um post excluindo o jogo no endpoint "/game/"
    E deve retornar um body com a mensagem "game is no longer alive"