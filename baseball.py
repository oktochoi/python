from random import randint


def generate_numbers():
    numbers = []
    for y in range(3):
        x = randint(0,9)
        if x in numbers:
            x = randint(0,9)
        numbers.append(x)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    count = 0

    while count <= 2:
        x = int(input("{}번째 숫자를 입력하세요: ".format(count+1)))
        if(x>9 or x<0):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요. ")
        elif(x in new_guess):
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(x)
            count +=1
    
    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    for x in range(3):
        if guesses[x] == solution[x]:
            strike_count +=1
        elif guesses[x] in solution:
            ball_count +=1
    print("{}S, {}B".format(strike_count,ball_count))

    return strike_count, ball_count

ANSWER = generate_numbers()
tries = 0
correct = False

while not correct:
    guess = take_guess()
    strikes, balls = get_score(guess, ANSWER)
    if strikes == 3:
        correct = True
    tries += 1

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))