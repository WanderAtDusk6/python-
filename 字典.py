score={
    'm':95,
    's':97,
    'j':87
    }
#print(score['m'])

for name in score:
    print(score[name])

score['ms']=0
score['j']=59
del score['s']

for name in score:
    print(name,score[name])


