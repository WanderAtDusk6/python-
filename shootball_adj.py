from random import choice

score=[0,0]
direction=['left','center','right']

def kick():
    print('=======you kick======')
    print('left,center,right')
    you=input()
    print('you kicked '+you)

    print()
    keeper=choice(direction)
    print('computer saved '+keeper)
    print()

    if you !=keeper:
        print('    Goal!!!')
        score[0]+=1
    else:
        print('    oop......')
        score[1]+=1
    print('Score:%d(you)-%d(keeper)\n'%(score[0],score[1]))

    print('========you save=====')#类似上面，略

for i in range(1):
    print('====Round %d======'%(i+1))
    kick()

while(score[0]==score[1]):
    i+=1
    print('====Round %d======'%(i+1))
    kick()

if score[0]>score[1]:
    print('you win!')
else:
    print('you lose!')
