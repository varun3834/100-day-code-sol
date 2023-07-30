import random
t=["stone","paper","scissor"]

def win():
    if bot == p:
        print(f'draw match')
    
    elif t[player-1] == bot :
        print(f'won by you')
        
        
    else:
        print("bot win")
        
while True:
    bot=random.choice(t)
    player=int(input('''type 1 for stone 
    2 for paper
    3 for scissor:  '''))-1
    p=t[player]
    print(p)
    print(f'{bot} choosen by bot')
    win()
    # a=(input("wanted to continue press y else n: ")).lower
    
    # if a=="y":
    #     pass
    # elif a=="n":
    #     break
    # else:
    #     pass
        
        
# def bot():
#     t=["stone","paper","scissor"]
#     bot1=random.choice(t)
#     print(bot1)

# def player():
#     t=["stone","paper","scissor"]
#     player=int(input('''type 1 for stone 
#             2 for paper
#             3 for scissor:  '''))-1
#     player=t[player]
#     print(player)
# player()
# bot() 
# print('''choosen by bot''')

    # bot="stone"
    #player="stone"



# print(f'{bot()} bot choosen ')

    
    