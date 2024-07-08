import random
with open('vocabulary.txt','r',encoding='UTF-8') as f:
        for line in f:              
            data =  line.strip().split(": ")
            answer = data[0]
            x = input("{} :".format(data[1]))
            if x == answer:
                  print("맞았습니다!\n")
            else:
                  print("틀렸습니다! 정답은 {} 입니다\n".format(data[0]))