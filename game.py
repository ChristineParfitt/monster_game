
game_running = True

while game_running == True :
    new_round = True
    player = {'name': 'Christine', 'attack': 19, 'heal': 16, 'health': 100}
    monster = {'name': 'Max', 'attack': 12, 'health': 100}  
    while new_round == True :
        player_won = False
        monster_won = False

        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit game')

        player_choice = input()

        if player_choice == '1' : 
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0 :
                    player_won = True
            else :
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0 :
                    monster_won = True


            print(monster['health'])
            print(player['health'])

        elif player_choice == '2' :
            print('Health')
        elif player_choice == '3' :
            game_running = False
            new_round = False

        else :
            print('Error')
        
        if player_won == True or monster_won == True :
            #player['health'] = 100
            #monster['health'] = 100
            new_round = False
            print('New round!')

# up to 50:39 on the youtube video: https://youtu.be/kDdTgxv2Vv0
