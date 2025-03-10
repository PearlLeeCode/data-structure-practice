def solution(myString):
    result = ""
    for char in myString:
        if char == "a":
            result += char.upper()
        else:
            result += char.lower()
    return result
