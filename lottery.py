from random import randint

def generate_numbers(n):
    """번호 뽑기"""
    lot_list = []
    for i in range(n):
        x = randint(1,45)
        lot_list.append(x)
    loto = sorted(lot_list)
    return loto

def draw_winning_numbers():
    """당첨 번호 뽑기"""
    winning_numbers = generate_numbers(6)
    bonus_number = randint(1,45)
    while bonus_number in winning_numbers:
        bonus_number = randint(1,45)        
    winning_numbers.append(bonus_number)
    return winning_numbers

def count_matching_numbers(numbers, winning_numbers):
    """겹치는 번호 개수"""
    count = 0

    for x in numbers:
        if x in winning_numbers:
                count +=1
                
    return count


def count_matching_numbers(numbers, winning_numbers):
    """겹치는 번호 개수"""
    count = 0

    for x in numbers:
        if x in winning_numbers:
                count +=1
                
    return count

def check(numbers, winning_numbers):
    """당첨 확인"""  
    count = count_matching_numbers(numbers, winning_numbers)
    money = 0
    if count == 6:
        if(winning_numbers[6] in numbers):
            money = 50000000
        else:
            money = 1000000000
    elif count == 5:
        money = 1000000
    elif count == 4:
        money = 50000
    elif count == 3:
        money = 5000
    
    return money
    
