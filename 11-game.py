import random 

options = ('piedra', 'papel', 'tijera')
rounds = 1


print("""
      [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
                  >>> Ingresa una opción <<<
      """)

def choose_options():

    user_option = input('>>> Piedra, papel o tijera => ')
    user_option = user_option.lower()
    
    if not user_option in options:
        print('Esa opción no es valida')
        return None, None
        
    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)

    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!\n')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('🪨 Piedra gana a tijera ✂️')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('📄 Papel gana a piedra 🪨')
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('📄 Papel gana a piedra 🪨')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('✂️ Tijera gana a papel 📄')
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('✂️ Tijera gana a papel 📄')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('🪨 Piedra gana a tijera ✂️')
            print('¡Computer gana!\n')
            computer_wins += 1
    
    return user_wins, computer_wins


def run_game():

    computer_wins  = 0 
    user_wins      = 0
    current_rounds = rounds

    while True:
        print('***' * 10)
        print('Round ', current_rounds)
        print('***' * 10)
        
        print(f'''
    🤖 Computer wins: {computer_wins}
    🙋 User wins: {user_wins}
            ''')
        
        current_rounds += 1

        user_option, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if user_wins == 3:
            print('🎖️ El ganador es User 🎖️')
            break

        if computer_wins == 3:
            print('🎖️ El ganador es Computer 🎖️')
            break

if __name__ == '__main__':
    run_game()
