def solution(names):
    answer = []
    # names 리스트의 원소들이 5로 나눴을때 나머지가 0이면 answer 리스트에 append 한다. 
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(names[i])
    return answer


# other source code
# 5칸의 배수로 뛰어 names리스트의 값을 반환한다. 
def solution(names):
    return names[::5]