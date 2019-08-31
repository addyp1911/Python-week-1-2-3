# ----------------------------------Deckofcards prg-----------------------------------------------
# -Deckofcards.py
# date : 30/08/2019
# method to print the shuffle the cards using Random method and then
# distribute 9 Cards to 4 Players and Print the Cards the received by the 4 Players

import random
suit=["heart","spade","diamond","club"]
rank=["ace","2","3","4","5","6","7","8","9","jack","queen","king"]


#method to shuffle the cards among user entered no of players
def shufflecards(player_num,cards):
    my_list=[]
    for i in suit:
        for j in rank:
            my_list.append(i+" "+j)

    matrix=[]
    for i in range(player_num):
        player=[]
        for j in range(cards):
            card=random.choice(my_list)
            player.append(card)
            my_list.remove(card)
            player.sort()    
        matrix.append(player)
    
    #to print the header of the display as player names
    for i in range(0,player_num):
        print("player{}".format(i+1),end="\t")

    #method to print the shuffled cards among user entered no of players
    for i in matrix:
        for j in range(len(i)):
            if(j % player_num == 0):
                print()
            print(' {} \t'.format(i[j]),end='')