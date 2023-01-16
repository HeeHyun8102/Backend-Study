<<<<<<< HEAD:algorithm/김희현/2주차/programmers_StackQueue1.py
def solution(arr):
    
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)

    return answer
    
=======
def solution(arr):
    
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)

    return answer
>>>>>>> 605cb84ff60988ee601524ce539eae2cfa9af5d9:algorithm/김희현/week2_StackQueue/programmers_StackQueue1.py
