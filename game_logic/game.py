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

    war_pile = []

    war_count = 0
    if round_winner == "WAR":
        if len(player_1['hand']) > 1 and len(player_2['hand']) > 1:
            print("WAR")

            
            
            war_pile.append(player_1_card)
            war_pile.append(player_2_card)
            
            for i in range(3):
                if len(player_1['hand']) > 1 and len(player_2['hand']) > 1:
                    war_pile.append(player_1['hand'].pop())
                    war_pile.append(player_2['hand'].pop())
                    print("3 face down cards added to war pile")
                else:
                    print("out of cards for war, starting final battle")
                    break

            print("initiating war round")
            play_round(player_1,player_2)
        else:
            print("last round ended in war")
            war_count += 1
            print(f"starting world war {war_count}")
            game = init_game()
            playing = True
            while playing:
                if len(game['player_1']['hand']) > 0 and len(game['player_2']['hand']) > 0:
                    play_round(game['player_1'], game['player_2'])
                        
                else:
                    if len(game['player_1']['won_pile']) == len(game['player_2']['won_pile']):
                        print("tie")
                        playing = False

                    elif len(game['player_1']['won_pile']) > len(game['player_2']['won_pile']):
                        print(f"{game['player_1']['name']} won world war {war_count}!")
                        playing = False

                    elif len(game['player_1']['won_pile']) < len(game['player_2']['won_pile']):
                        print(f"{game['player_2']['name']} won world war {war_count}!")
                        playing = False
        
            
        
    elif round_winner == "p1":
        player_1['won_pile'].append(player_1_card)
        player_1['won_pile'].append(player_2_card)
        print(f"{player_1['name']} has won the round!")
    elif round_winner == "p2":
        player_2['won_pile'].append(player_1_card)
        player_2['won_pile'].append(player_2_card)
        print(f"{player_2['name']} has won the round!")
        
