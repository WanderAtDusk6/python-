from random import choice

score_you=0
score_keeper=0
direction=['left','center','right']

for i in range(0,5):
    print('=====Round %d-you kick!====='%(i+1))
    print('choose one side to shoot?')
    print('left,center,right')
    
    you=input()
    print('you kicked '+you)
    print()
    
    keeper=choice(direction)
    print('goalkeeper save '+keeper)
    if you  !=keeper:
        print('goal!!!')
        score_you+=1
    else:
        print('oops....')
        score_keeper+=1
    print('Score:%d(you)-%d(keeper)'%(score_you,score_keeper))
    print()
        
