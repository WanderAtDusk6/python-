from random import randint

#账号
name=input('请输入你的名字：')#输入玩家ID

f=open('f:/pythonsaver/output_txt_存放处/zzgame.txt')
lines=f.readlines()
f.close()

scores={}   #字典初始化
for l in lines:
    s=l.split()   #把每行数据拆分成列表（记录为s）
    scores[s[0]]=s[1:]  #第一项数据作为key,剩下的作为value
score=scores.get(name)  #查找当前玩家的数据
if score is None:   #如果它不存在
    score=[0,0,0]   #玩家数据初始化
    
#游戏数据
game_times=int(score[0])
min_times =int(score[1])
total_times=int(score[2])

if game_times>0:
    avg_times=float(total_times/game_times)
else:
    avg_times=0

#运行
print('你已经玩了%d次，最少%d猜出答案，平均%.2f猜出答案'%(game_times,min_times,avg_times))

num = randint(1,100)
times=0    #记录游戏局数
print('Guess what I think?')
bingo= False

while bingo==False:
    times+=1   #轮数加一
    answer = int(input())
    
    if answer<num:
        print(str(answer)+' is too small!')
        
    if answer>num:
        print('%s is too big!'%answer)
    if answer==num:
        print('BINGO!\n%s is right answer.'%answer)
        bingo=True
    if answer==0:        #use for test
        print('Tip: this number is %d'%num)

#第一次玩；或这次轮数比最小轮数要小，则更新最小轮数
if game_times == 0 or times<min_times:
    min_times = times
total_times += times   #total times up!
game_times+=1      #game times up!

#玩家ID及数据录入
scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''   #result初始化，用于存储数据
for n in scores:
    #格式化name，game_times,min_times,total_times
    #注 结尾加上\n换行
    line =n+' '+' '.join(scores[n]) + '\n'
    result+=line #添加进result

f=open('f:/pythonsaver/output_txt_存放处/zzgame.txt','w')
f.write(result)
f.close()


#备注
#scores为字典
#l 存储原文件每行的数据；s为行数据的split
#之后scores通过s[] 将第一项之后的作为值，第一项为key




















