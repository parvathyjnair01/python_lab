import random
while True:
    game=["rock","paper","scissors"]
    choice=(input("Your options are rock,paper or scissors\n[type 'exit' to quit]\nchoose:"))
    comp_choice=random.choice(game)
    print (choice)
    print(comp_choice)
    if choice=='paper'and comp_choice=='rock':
        print('You Win!')
    elif choice=='scissors'and comp_choice=='paper':
        print('You Win!')
    elif choice=='rock'and comp_choice=='scissors':
        print('You Win!')
    elif comp_choice==choice:
        print('Its a tie')
    else:
        print ('you loose')





