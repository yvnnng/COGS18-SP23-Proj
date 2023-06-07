"""Testing for my functions.
"""
import mock
import builtins
from functions import end_game, refresher, head_count, after_action

def test_end_game():
    """Checks to see if user input is the string 'quit' then returns a statement."""
    
    lt_input = 'quit'
    
    assert type(end_game(lt_input)) == str
    assert len(end_game(lt_input)) == 35
    assert end_game(lt_input) == 'Good work, train harder next time💪!'
    
    
def test_refresher():
    """Checks to see if the user input is valid and matches the tactic provided."""
    
    refresher_training = ['Column: Permits fire and maneuver to the flanks',
                          'Line: Permits maximum firepower to the flanks',
                          'Echelon left/right: Permits firepower to the front and direction specified',
                          'Wedge: Permits firepower to all directions, especially flanks',
                          'Vee: Permits firepower to all directions, especially rear']
    
    assert callable(refresher)
    assert type(refresher(tactic = refresher_training[0], lt_input='T')) == str
    assert refresher(tactic = refresher_training[0], lt_input = 'T') == 'Correct✅'
    assert refresher(tactic = refresher_training[0], lt_input = 'F') == 'Incorrect❌'
    assert refresher(tactic = refresher_training[0], lt_input = 'quit') == 'Good work, train harder next time💪!'
    assert refresher(tactic = refresher_training[0], lt_input = 'asdf') == 'Your answer is not a tactic, Lt, stop operating out of bounds!'
    assert refresher(tactic = refresher_training[0], lt_input = 1234) == 'Your answer is not a tactic, Lt, stop operating out of bounds!'


def test_head_count():
    
    assert callable(head_count)
    
    x = 'x'
   
    with mock.patch.object(builtins, 'input', lambda _: x*13):
        
        accountability = head_count()
        assert type(accountability) == str
        assert accountability == 'complete'
        
    with mock.patch.object(builtins, 'input', lambda _: '123'):

        accountability = head_count()
        assert type(accountability) == str
        assert accountability == 'complete'
        
    with mock.patch.object(builtins, 'input', lambda _: 'quit'):

        accountability = head_count()
        assert type(accountability) == str
        assert accountability == 'incomplete'
        
    
def test_after_action():
    
    squad_tacts = ['column', 'line', 'echelon left', 'echelon right', 'wedge', 'vee']
    
    scenarios = ['Ambush fire from the left!', 
                'Ambush fire from the right!',
                'Ambush fire from the front!',
                'Ambush from the front and left flank!',
                'Ambush from the front and right flank!',
                'Ambush from all directions, heavy fire from the front!',
                'Ambush from all directions, heavy fire from the rear!']
    
    ambush = scenarios 
    
    assert callable(after_action)
    
    assert after_action(scenarios[0], 'column', 13, squad_tacts) == 13
    
    outcome = after_action(scenarios[0], 'line', 13, squad_tacts)
    assert outcome in (10, 11, 12)
    