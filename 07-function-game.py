# Imports
import random
import time
import getpass

# Write animation
def write_fx(frase):
    for letra in frase:
        print(letra, end='', flush=True)
        time.sleep(0.010)
    
# game
def play(num1, num2, cpu_cs):
     
    empty = 0

    computer_wins = 0

    user_wins = 0

    rounds = 0


    while True:
        
        num2 = random.choice(cpu_cs)


        if num1 == num2:
            time.sleep(1)
            result = '\n    [*] Nadie gana'
            empty += 1
            rounds += 1

        elif num1 =='tijeras' and num2 == 'piedra' or num1 == 'papel' and num2 == 'tijeras' or num1 == 'piedra' and num2 == 'papel':
            time.sleep(1)
            result = '\n    [*] La maquina gana'
            computer_wins += 1
            rounds += 1

        elif num1 == 'piedra' and num2 == 'tijeras' or num1 == 'tijeras' and num2 == 'papel' or num1 == 'papel' and num2 == 'piedra':
            time.sleep(1)
            result = '\n    [*] El jugador gana'
            user_wins += 1
            rounds += 1

        if user_wins == 2:
            write_fx(f'''   
    Resultado de Partida numero {rounds}   
                
            {result}

    La seleccion de la maquina fue {num2}''')
            table('EL Usuario :D', rounds, user_wins, computer_wins, empty)
            break

        elif computer_wins == 2:
            write_fx(f'''   
    Resultado de Partida numero {rounds}   
                
            {result}

    La seleccion de la maquina fue {num2}''')
            table('La Maquina :D', rounds, user_wins, computer_wins, empty)
            break

        else:
            write_fx(f'''   
    RESULTADO DE PARTIDA NUMERO {rounds}   
                
            {result}

    La seleccion de la maquina fue {num2}''')

                
            write_fx(f'''
            
    vuelve a escoger entre 
            
    [*] Piedra
    [*] Papel
    [*] Tijeras
            
    para la siguiente ronda: ''')
            
            num1 = input('').lower().replace(' ','')

            if num1 not in cpu_cs:
                write_fx('\n    Comando no valido')
                time.sleep(1)
                
                write_fx(f'''
            
    vuelve a escoger entre 
            
    [*] Piedra
    [*] Papel
    [*] Tijeras
            
    para la siguiente ronda: ''')
                num1 = input('').lower().replace(' ','')
                continue

# User Interface
def table(nom, var1, var2, var3, var4):
    time.sleep(1)
    write_fx(f'''
    
     ________________________________________________________________
    | Partidas | ganadas por usuario | ganadas por maquina | Empates |
    |------------------------------------------------------|---------|
    |     {var1}    |         {var2}           |         {var3}           |    {var4}    |
     ----------------------------------------------------------------
    
    El ganador de la ronda es  {nom} 

                        
                        
                         ██████╗   ██████╗
                        ██╔════╝  ██╔════╝
                        ██║░░██╗  ██║░░██╗
                        ██║░░╚██╗ ██║░░╚██╗
                        ╚██████╔╝ ╚██████╔╝
                         ╚═════╝   ╚═════╝

    ''')


def home():
    choices = ('piedra', 'papel', 'tijeras')

    write_fx ('''
    
    Bienvenido a piedra, papel o tijeras

    El juego es en partidas, el primero en ganar
    2 partidas gana la ronda.

    [*] Piedra
    [*] Papel
    [*] Tijeras
    
    Escribe cual va a escoger aca --> ''')

    user_cs = input('').lower().replace(' ','')

    comp_cs = random.choice(choices)

    if user_cs not in choices:
        write_fx('\n    Comando no valido')
        time.sleep(1)
        home()

    else:
        play(user_cs, comp_cs, choices)

        write_fx(f'\n\n    Preciona enter para volver a jugar')
        getpass.getpass(' ')
        home()

if __name__ == '__main__':
    home()