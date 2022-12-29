def game_instructions():
    print("""\tInstrucciones del juego
    selecciona la opción con la cual vas a atacar :
    1. ==> Piedra 🪨
    2. ==> Papel 🧻
    3. ==> Tijeras ✂️
    """)

    input('¡Listo! presiona ---ENTER--- para comenzar 😎 ')

def num_partidas(): 
    rounds = int(input("¿Cuántas partidas quieres jugar? "))
    return rounds

def star_game():
    print(""""¡¡¡¡¡¡¡¡¡¡COMIENZA EL JUEGO!!!!!!!!!!!!!!""")

def rounds_count(numero_partidas):
    print(f"""*************
ROUND {numero_partidas}
*************""")

def pause():
    input("Presiona enter para continuar")

def contador_resultados(victorias, derrotas, empates, rounds):
    print(f"""Resultados de la contienda:

De {rounds} partidas...

El numero de victorias fue de: {victorias}
El número de derrotas fue de: {derrotas}
El número de empates fue de: {empates}""")

def end():
    print("Gracias por haber jugado el mítico juego de piedra papel o tijeras")



    

