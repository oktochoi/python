import random
with open('vocabulary.txt','r',encoding='UTF-8') as f:
        
        lines = f.readlines()  # 파일의 모든 줄을 읽어 리스트로 저장
        len = len(lines)

        while True:
            ran = random.randint(0,len-1)              
            line = lines[ran].strip()
            data =  line.split(": ")
            answer = data[0]
            if len(data) != 2:  
                    continue
            x = input("{} :".format(data[1]))
            if answer == "q":
                break
            if x == answer:
                  print("맞았습니다!\n")
            else:
                  print("틀렸습니다! 정답은 {} 입니다\n".format(data[0]))
# f만큼 랜덤
# 사전 만들기