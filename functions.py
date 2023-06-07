"""A collection of functions for executing my game."""

import time
import random
from IPython.display import clear_output

def type_msg(msg, delay = 0.05):
    """Takes in a string and outputs the message using a typewriter effect.
    
    Parameters
    ----------
    msg : string
        String that stores the message that will be operated on.
        
    delay : float
        Determines length of time before displaying the next character.
        
    Returns
    -------
    print() : string
        String will be displayed as a typed message.
        
    References
    ----------
    .. [1] Open AI: ChatGpt - Learned how to use the argument 'flush = True'
    to immediately display the following output to create a typewriter effect.
    """ 
    for ltr in msg:
        
        # default python buffers outputs, we override using 'flush = True' 
        print(ltr, end='', flush = True)
        time.sleep(delay)
    
    print()


def opening_msg():
    """Displays opening messages with a typewriter effect, then prompts user for input.
    
    Parameters
    ----------
    None
        
    Returns
    -------
    lt_input : string
        String containing the user input. 
        
    References
    ----------
    .. [1] Open AI: ChatGpt - https://chat.openai.com/ 
    Learned how to use the input() to prompt user for an input.
    .. [2] Stack Overflow - https://stackoverflow.com/questions/24816237/ipython-notebook-clear-cell-output-in-code
    Learned how to import and use clear_output() to erase outputs. 
    """ 
    # displaying messages on separate lines for readability 
    type_msg('Lt! You have been tasked to lead a patrol with 13 Marines.'
            '\nCurrent intel reports indicate that ambushes are likely. Stay frosty.'
            '\nTime to refresh your memory with patrolling tactics...')
    
    time.sleep(2)
    
    # using this clear_output() to remove opening messages for a clean slate
    # then prompt user for input
    clear_output(wait = True)
    lt_input = input('Enter y to begin:')
    
    clear_output(wait = False)
    
    return lt_input
    

def end_game(lt_input):
    """Checks if input matches specific value, then returns a string.
    
    Parameters
    ----------
    lt_input : string
        String that stores the value that the conditional checks for.
        
    Returns
    -------
    out : string
        String that displays a message. 
        
    References
    ----------
    .. [1] IA: Lillian Ho - https://emojipedia.org/
    Learned how to copy and paste emojis into strings.
    """ 
    
    if lt_input == 'quit':
        out = 'Good work, train harder next time💪!'
        time.sleep(2)
    
    return out


refresher_training = ['Column: Permits fire and maneuver to the flanks',
                     'Line: Permits maximum firepower to the flanks',
                     'Echelon left/right: Permits firepower to the front and direction specified',
                     'Wedge: Permits firepower to all directions, especially flanks',
                     'Vee: Permits firepower to all directions, especially rear']

def refresher(tactic, lt_input):
    """Checks if the user input is the correct response to the tactic displayed.
    
    Parameters
    ----------
    tactic : string
        Determines what tactic from the list is displayed.
        
    lt_input : string
        String that stores user input.
        
    Returns
    -------
    out : string
        String that stores the result of the conditional that was met. 
    """ 
    
    if tactic in refresher_training and lt_input in ['T', 'F']:
        
        if tactic == refresher_training[0] and lt_input == 'T':
            out = 'Correct✅'
    
        elif tactic == refresher_training[1] and lt_input == 'F':
            out = 'Correct✅'
        
        elif tactic == refresher_training[2] and lt_input == 'T':
            out = 'Correct✅'
        
        elif tactic == refresher_training[3] and lt_input == 'F':
            out = 'Correct✅'
        
        elif tactic == refresher_training[4] and lt_input == 'T':
            out = 'Correct✅'
            
        else:
            out = 'Incorrect❌'
    
    # allows user to quit the game
    elif lt_input == 'quit':
        out = end_game(lt_input)
    
    # addresses when user inputs random values
    else:
        out = 'Your answer is not a tactic, Lt, stop operating out of bounds!'     
        
    return out
    

def start_training():
    """Runs through all the tactics, calls the refresher() to check user input, 
    then displays training results.
    
    Parameters
    ----------
    None
        
    Returns
    -------
    training_results : string
        String that stores whether training was complete or incomplete.
    """ 
    # used for loop to quiz user on all tactics stored in the refresher_training list
    for tactic in refresher_training:
        print(tactic)
        time.sleep(1)
    
        lt_input = input('Enter T for True or F for False: ')
        
        # checks user input and displays the results for the user
        accuracy = refresher(tactic, lt_input)
        print(accuracy)
        time.sleep(3)
    
        clear_output(wait = True)
    
        # allows user to quit the game by breaking out of the loop
        if accuracy == 'Good work, train harder next time💪!':
            training_results = 'incomplete'
            break
    
        training_results = 'complete'
    
    clear_output(wait = True)
    
    return training_results    
    

    
def head_count():
    """Prompts the user for an input, checks if user input is accurate,
    then displays the string of the conditional that was met.
    
    Parameters
    ----------
    None
        
    Returns
    -------
    accountability : string
        String that stores the result of the conditional that was met.
    """ 
    
    lt_input = input('You begin your head count...enter x for each Marine:')

    x = 'x'
    
    # allows user to quit the game
    if lt_input == 'quit':
        out = end_game('quit')
        print(out)
        time.sleep(3)
        clear_output(wait = False)
        
        accountability = 'incomplete'
    
    elif lt_input == x*13:
        print('All Marines accounted for!🫡')
        time.sleep(3)
        clear_output(wait = False)
        
        accountability = 'complete'
        
    # provides user a second try to enter the right input    
    else:
        print('Where is Private Smuckatelli??🙄')
        recount = input('Enter x for each Marine:')
        
        x = 'x'
          
        if recount == x*13:
            print('All Marines accounted for!🫡')
            time.sleep(3)
            clear_output(wait = False)
            
            accountability = 'complete'
        
        # allows user to move forward even if second try is wrong
        else:
            print('Can you count, Lt?? 11, 12, 13, move out!😤')
            time.sleep(3)
            clear_output(wait = False)
            
            accountability = 'complete'
    
    return accountability


def after_action(ambush, lt_input, squad_size, squad_tacts):
    """Checks if user input is in a list and if it matches
    the ambush input, then returns a new value for squad size. 
    
    Parameters
    ----------
    ambush : string
        Determines what ambush from the list is displayed.
        
    lt_input : string
        String that stores user input.
        
    squad_size : int
        Integer denoting how many Marines exist.
        
    squad_tacts : list
        List of all the squad tacts. 
        
    Returns
    -------
    squad_size : int
        Integer that stores the result of the user input. 
    """ 
    
    if lt_input in squad_tacts:           
        
        if ambush == 'Ambush fire from the left!' and lt_input == 'column':
            print('Threat eliminated.🛡️')
            squad_size = squad_size
        
        elif ambush == 'Ambush fire from the right!' and lt_input == 'column':
            print('Threat eliminated.🛡️')
            squad_size = squad_size
    
        elif ambush == 'Ambush fire from the front!' and lt_input == 'line':
            print('Threat eliminated.🛡️')
            squad_size = squad_size
        
        elif ambush == 'Ambush from the front and left flank!' and lt_input == 'echelon left':
            print('Threat eliminated.🛡️')
            squad_size = squad_size
    
        elif ambush == 'Ambush from the front and right flank!' and lt_input == 'echelon right':
            print('Threat eliminated.🛡️')
            squad_size = squad_size
            
        elif ambush == 'Ambush from all directions, heavy fire from the front!' and lt_input == 'wedge':
            print('Threat eliminated.🛡️')
            squad_size = squad_size
    
        elif ambush == 'Ambush from all directions, heavy fire from the rear!' and lt_input == 'vee':
            print('Threat eliminated.🛡️')
            squad_size = squad_size
        
        # addresses when user input is wrong
        else:
            print('Doc! Marine down! Marine down!📢')
            
            random_kills = random.choice((1, 2, 3))
            if random_kills == 1:
                print('☠️')
            elif random_kills == 2:
                print('☠️☠️')
            elif random_kills == 3: 
                print('☠️☠️☠️')
                
            squad_size = squad_size - random_kills
            if squad_size < 0:
                squad_size = 0
    
    # allows user to quit the game
    elif lt_input == 'quit':
        end_game(lt_input)
        squad_size = 0
    
    # addresses when user inputs random values
    else: 
        print("Get your head in the game, Lt, that's not a tactic!")
    
    print('Lt, you now have ' + str(squad_size) + ' Marines!')
    
    return squad_size

def patrolling():
    """Provides a scenario and prompts user for input,
     then measures length of time user takes to respond
     and displays results of user input and time. 
    
    Parameters
    ----------
    None
        
    Returns
    -------
    decision_times : list
        List of times measured for user to answer each scenario. 
        
    References
    ----------
    .. [1] IA: Lillian Ho - Suggested using time() to measure time.
    .. [2] Open AI: ChatGpt - https://chat.openai.com/ 
    Learned how to use the round() to simplifying a long float into 3 decimal places. 
    """ 
    
    squad_size = 13
    
    squad_tacts = ['column', 'line', 'echelon left', 'echelon right', 'wedge', 'vee']
    
    scenarios = ['Ambush fire from the left!', 
                'Ambush fire from the right!',
                'Ambush fire from the front!',
                'Ambush from the front and left flank!',
                'Ambush from the front and right flank!',
                'Ambush from all directions, heavy fire from the front!',
                'Ambush from all directions, heavy fire from the rear!']
    
    decision_times = []
    
    while squad_size > 0:
        
        ambush = (random.choice(scenarios))
        print(ambush)
        print('Your options are column, line, echelon left, echelon right, wedge, or vee.')
    
        start_time = time.time()

        lt_input = input('Choose your squad formation:')
    
        end_time = time.time()
        
        # measures the time user takes to provide an input, rounds the float and displays the time, 
        # then adds it to a list which will displayed at the end
        decision_time = round(end_time - start_time, 3)
        decision_times.append(decision_time)
        print(f"Time: {decision_time} seconds")
    
        squad_size = after_action(ambush, lt_input, squad_size, squad_tacts)
        
        time.sleep(4)
        
        clear_output(wait = True)
    
        # addresses when user loses all Marines and the game ends
        if squad_size == 0:
            print('Hit the books📗📚! Read up on RP0501 Patrolling Tactics!')
            print('decision times = ' + str(decision_times))
            time.sleep(3)
            clear_output(wait = True)
            break

def start_game(): 
    """Initiates the functions in order to execute the game. 
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """ 
    
    lt_input = opening_msg()
    
    if lt_input == 'y':
        
        refresher_results = start_training()
        
        # allows user to quit during refresher training
        if refresher_results == 'incomplete':
            end_game('quit')
        
        elif refresher_results == 'complete':
            
            accounted = head_count()
            
            # allows user to quit during head count
            if accounted == 'incomplete':
                end_game('quit')
                
            elif accounted == 'complete':
                patrolling()
    
    # allows user to quit when first prompted for input
    elif lt_input == 'quit':
        end_game('quit')
        