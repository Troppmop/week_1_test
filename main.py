from game_logic.game import *

if __name__ == "__main__":
    
    
    def play():
        game = init_game()
        playing = True
        while playing:
            if len(game['player_1']['hand']) > 0 and len(game['player_2']['hand']) > 0:
                play_round(game['player_1'], game['player_2'])
                        
            else:
                if len(game['player_1']['won_pile']) == len(game['player_2']['won_pile']):
                
                    print("tie")
                    print("starting NUCLEAR war")
                    play()
                    playing = False
                    

                elif len(game['player_1']['won_pile']) > len(game['player_2']['won_pile']):
                    print(f"{game['player_1']['name']} won the war!")
                    playing = False

                elif len(game['player_1']['won_pile']) < len(game['player_2']['won_pile']):
                    print(f"{game['player_2']['name']} won the war!")
                    playing = False
            
    play()
