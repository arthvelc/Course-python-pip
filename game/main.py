# mítico juego de piedra papel o tijeras
#vamos a empezar a programar de verdad 
#jaja rompí el código, pero luego lo arreglo, mientras este código servirá para fines prácticos 20/dic/2022.
#Ya estructuré  mejor el programa modularizando procesos en el algoritmo :D  29/12/22
import random
import os
import showscreen as show
import game_rules as game

def clear():
    os.system('clear')
count=1
clear()
def run():
    show.game_instructions()
    clear()
    rounds= show.num_partidas() 
    clear()
    show.star_game()
    count=1
    while count<=rounds:
        show.rounds_count(count)
        victorias, derrotas, empates = game.game()
        show.pause()
        clear()
        count+=1
    show.contador_resultados(victorias, derrotas, empates, rounds)
    show.pause()
    clear()
    show.end()

if __name__== '__main__':
    run()















    
  
    

    