# 입력 받기
import sys
input = sys.stdin.read

# 입력 데이터 처리
data = input().strip().split('\n')

# 첫 번째 줄은 테스트 케이스의 개수 C
C = int(data[0])

results = []
for i in range(1, C + 1):
    # 각 테스트 케이스에서 첫 번째 수는 학생의 수 N
    case_data = list(map(int, data[i].split()))
    N = case_data[0]
    scores = case_data[1:]
    
    # 평균 계산
    average = sum(scores) / N
    
    # 평균을 넘는 학생들의 비율 계산
    count_above_average = sum(1 for score in scores if score > average)
    ratio_above_average = (count_above_average / N) * 100
    
    # 소수점 셋째 자리까지 반올림하여 출력 형식에 맞추기
    results.append(f"{ratio_above_average:.3f}%")

# 결과 출력
for result in results:
    print(result)
