def solution(numbers, n):
    total = 0  # 변수명 변경
    for num in numbers:
        total += num  # 바로 더하기
        if total > n:  # n을 초과하면 즉시 반환
            return total
    return total  # 모든 요소를 순회한 경우 반환
