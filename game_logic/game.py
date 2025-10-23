from utils.deck import *
def create_player(name:str="AI")->dict:
    player = {}

    hand = []

    won_pile = []
    
    player.update({'name':name})
    player.update({'hand':hand})
    player.update({'won_pile':won_pile})

    return player

def init_game()->dict:
    game = {}

    human = create_player("dovid")
    ai = create_player()

    deck = create_deck()
    deck = shuffle(deck)

    human['hand'] = deck[:26]
    ai['hand'] = deck[26:]

    game.update({'deck':deck})
    game.update({'player_1':human})
    game.update({'player_2':ai})
    
    return game

def play_round(player_1:dict,player_2:dict):
    player_1_card = player_1['hand'].pop()
    player_2_card = player_2['hand'].pop()

    print(f"{player_1['name']}'s card is {player_1_card}")
    print(f"{player_2['name']}'s card is {player_2_card}")
    
    round_winner = compare_cards(player_1_card,player_2_card)

    if round_winner == "WAR":
        print("WAR")
    elif round_winner == "p1":
        player_1['won_pile'].append(player_1_card)
        player_1['won_pile'].append(player_2_card)
        print(f"{player_1['name']} has won the round!")
    elif round_winner == "p2":
        player_2['won_pile'].append(player_1_card)
        player_2['won_pile'].append(player_2_card)
        print(f"{player_2['name']} has won the round!")
        
