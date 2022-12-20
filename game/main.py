# mítico juego de piedra papel o tijeras
#vamos a empezar a programar de verdad 
#jaja rompí el código, pero luego lo arreglo, mientras este código servirá para fines prácticos 20/dic/2022.
import random
import os

# A quí irán las funciones del juego 
def clear():
        os.system('clear')

def pcoption():
    return random.randrange(1,4)


def weaponuser(numero):
    if numero==1:
        print("""Perfecto, elegiste Piedra 🪨""")
    elif numero==2:
        print("""Perfecto, elegiste papel 🧻""")
    elif numero==3:
        print("""Perfecto, elegiste tijeras ✂️""")
    
def weaponpc(numero):
    if numero==1:
        print("""La computadora eligió Piedra 🪨""")
    elif numero==2:
        print("""La computadora eligió Papel 🧻""")
    elif numero==3:
        print("""La computadora eligió ✂️""")

#Aquí empieza a correr el programa-------------------->
 


clear()#clear proviene de la función de limpiado de pantalla
print("""\tInstrucciones del juego
selecciona la opción con la cual vas a atacar :
1. ==> Piedra 🪨
2. ==> Papel 🧻
3. ==> Tijeras ✂️
""")

input('¡Listo! presiona ---ENTER--- para comenzar 😎 ')

clear()

#Se pide el numero de partidas que se desea corrrer
'''rounds = int(input("¿Cuántas partidas quieres jugar? "))
num_partida=1'''
    

clear()
print(f""""¡¡¡¡¡¡¡¡¡¡COMIENZA EL JUEGO!!!!!!!!!!!!!!"
*************
ROUND 1
*************""")

userOption = int(input('Elige tu arma ==> '))#Seleccioon de la optión del jugador 
#Selección de armas 
if userOption==1:
    print("""Elegiste Piedra 🪨""")
elif userOption==2:
    print("""Elegiste Papel 🧻""")
elif userOption==3:
    print("""Elegiste tijeras ✂️""")

computerOption= pcoption()
if computerOption==1:
    print("""La Computadora Eligió Piedra 🪨""")
elif computerOption==2:
    print("""La computadora Eligió Papel 🧻""")
elif computerOption==3:
    print("""La computadora eligió Tijeras ✂️""")

#Aquí irá la regla del juego, quien gana y quien pierde.

if computerOption==userOption:
        print("Empate")
else:
    if computerOption==1 and userOption==2:
        print("Ganaste")
    elif computerOption==1 and userOption==3:
        print("Perdiste")
    elif computerOption==2 and userOption==1:
        print("perdiste")
    elif computerOption==2 and userOption==3:
        print("Ganaste")
    elif computerOption==3 and userOption==1:
        print("perdiste")
    else: 
        print("Ganaste")
#Hasta aquí todo va bien, dejaré esto para el curso, mañana o el sábado continuo con el mejoramiento del código











    
  
    

    