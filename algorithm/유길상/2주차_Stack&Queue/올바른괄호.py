#https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    stack = []
    is_right = False

    if len(s) % 2 != 0 or s[0] == ')':
        return is_right

    for i in range(0,len(s)):
        if s[i] == '(' :
            stack.append(s[i])
        elif s[i] == ')':
            stack.pop()    

    if len(stack) != 0:
        return is_right
    else :
        is_right = True
        return is_right