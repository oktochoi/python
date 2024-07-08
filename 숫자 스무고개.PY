import random
answer = random.randint(0,20)

def num(i):
    n =0
    for x in range(i):
        
        guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(i-n)))
        if(guess>answer):
            print("down")
        elif(guess<answer):
            print("up")
        elif(guess==answer):
            print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(n))
            exit()
        n+=1
        
i = int(input("몇 번의 기회를 원하시나요? "))
num(i)

import random
answer = random.randint(0,20)

guess = int(input("기회가 4번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
if(guess>answer):
    print("down")
elif(guess<answer):
    print("up")
elif(guess==answer):
    print("축하합니다. 1번 만에 숫자를 맞히셨습니다.")
    exit()

guess = int(input("기회가 3번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
if(guess>answer):
    print("down")
elif(guess<answer):
    print("up")
elif(guess==answer):
    print("축하합니다. 2번 만에 숫자를 맞히셨습니다.")
    exit()

guess = int(input("기회가 2번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
if(guess>answer):
    print("down")
elif(guess<answer):
    print("up")
elif(guess==answer):
    print("축하합니다. 3번 만에 숫자를 맞히셨습니다.")
    exit()

guess = int(input("기회가 1번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
if(guess>answer):
    print("아쉽습니다. 정답은 {}입니다.".format(guess))
elif(guess<answer):
    print("아쉽습니다. 정답은 {}입니다.".format(guess))
elif(guess==answer):
    print("축하합니다. 4번 만에 숫자를 맞히셨습니다.")