def solution(s):
    l = list(s)
    if l[0] == '(' and l[-1] == ')':
        if l.count('(') == l.count(')'):
            return True
        else:
            return False
    else:
        return False