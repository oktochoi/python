with open('vocabulary.txt', 'a', encoding='UTF-8') as f:  # Open the file in append mode

    while True:
        x = input("영어 단어를 입력하세요 (종료하려면 'q' 입력): ")
        if x == "q":
            break
        y = input("한국어 뜻을 입력하세요 (종료하려면 'q' 입력): ")
        if y == "q":
            break
        f.write("{} : {}\n".format(x,y))