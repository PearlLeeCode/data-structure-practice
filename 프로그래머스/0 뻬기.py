# 내가 푼 코드
def solution(n_str):
    #0이 아닌 숫자가 나오는 시점을 기준으로 삼는다. 
    for i in range(len(n_str)):
        if n_str[i] != '0':
            return n_str[i:]

# 더 쉬운 코드
def solution(n_str):
    return n_str.lstrip('0')

# 더 쉬운 코드 2 
def solution(n_str):
    return str(int(n_str)) # 이 과정에서 문자열 앞에 있는 불필요한 0이 제거된다. (예: "007" → 7)