from random import randint

msj = randint(1,100)
print('Guess what I think?')
bingo= False

while bingo==False:
    answer = int(input())
    
    if answer<msj:
        print(str(answer)+' is too small!')
        
    if answer>msj:
        print('%s is too big!'%answer)
    if answer==msj:
        print('BINGO!%s is right answer.'%answer)
        bingo=True
