def solution(myString):
    answer = []
    answer1 = []
    # x를 기준으로 문자열을 나눈다. 
    answer = myString.split('x')
    for i in answer:
        # i의 길이를 빈 리스트에 append한다. 
        answer1.append(len(i))
    return answer1
