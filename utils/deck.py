import random
def create_card(rank:str,suite:str)->dict:

    card_values = {'1':1,
                   '2':2,
                   '3':3,
                   '4':4,
                   '5':5,
                   '6':6,
                   '7':7,
                   '8':8,
                   '9':9,
                   '10':10,
                   'J':11,
                   'Q':12,
                   'K':13,
                   'A':14}

    value = card_values[rank]
    
    card = {}
    
    card.update({"rank":rank})
    card.update({"suite":suite})
    card.update({"value":value})
    
    return card

def compare_cards(p1_card:dict,p2_card:dict)->str:
    outcome = ""

    if p1_card['value'] == p2_card['value']:
        outcome = "WAR"
    elif p1_card['value'] > p2_card['value']:
        outcome = "p1"
    elif p1_card['value'] < p2_card['value']:
        outcome = "p2"
    
    return outcome

def create_deck()->list[dict]:
    deck = []
    rank_list = [
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
                '10',
                'J',
                'Q',
                'K',
                'A'
                ]

    suite_list = [
            "H",
            "C",
            "D",
            "S"
            ]
    
    for rank in range(14):
        card_rank = rank_list[rank]
        for suite in range(4):
            card_suite = suite_list[suite]
            deck.append(create_card(card_rank,card_suite))        
    
    return deck
    
def shuffle(deck:list[dict])->list[dict]:
    for i in range(1000):
        while True:
            index1 = random.randint(0,51)
            index2 = random.randint(0,51)
            if index1 != index2:
                break

        temp = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = temp 
    
    return deck
