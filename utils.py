import random as rd


def no_one_is_dead (my_lives:int,opponent_lives:int) -> bool:
    """Function wich verify that no one is dead.

    Args:
        my_lives (int): lives of the player
        opponent_lives (int): lives of the opponent 

    Returns:
        bool : True if no one is dead, False if someone is dead 
    """
    # Scores comparaison
    if my_lives <= 0 or opponent_lives <= 0:
        return False 
    else :
        return True 


def attack(player:str, opponent_lives: int, my_lives :int) -> int :
    
    damage = 0
    if player == 'you' :
        damage = rd.randint(5,10)
        opponent_lives -= damage
        if opponent_lives < 0 :
            opponent_lives = 0
    else :
        damage = rd.randint(5,15)
        my_lives -= damage
        if my_lives < 0 :
            my_lives = 0
    return opponent_lives, my_lives

def drink_potion(my_lives, potion):
    my_lives += (rd.randint(15,50))
    if my_lives >50 :
        my_lives = 50
    potion -= 1
    return my_lives, potion


def display_scores(opponent_lives, my_lives):
    print(f'Opponent has {opponent_lives} lives. I have {my_lives} lives.')

def who_won(my_lives, opponent_lives):
    if my_lives > opponent_lives:
        print('I won !!!!!')
    else : 
        print('Opponent won...')
    
            
def store_scores():
    pass

def menu(potion):
    if potion > 0 :
        choice = input('To attack, type 1. To drink potion, type 2.')
        if choice == "1" or choice == "2":
            return choice
        else : 
            print('Please type a correct value.')
            choice = input('To attack, type 1. To drink potion, type 2.')
    else :
        print("You don't have potion anymore. You will attack.")
        return "1" 
        
        
    