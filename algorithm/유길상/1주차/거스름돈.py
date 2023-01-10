# 춘향이는 편의점 카운터에서 일한다.
# 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 
# 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.
# 예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 
# 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

# solution 1
def main():
    cash = int(input())
    print(greedy_solution(cash))

def greedy_solution(cash : int) :
    # 5의 배수인지 확인
    remained_five = cash % 5
    # 5의 나머지 값이 짝수일 때 공식
    change_formula = ((cash // 5) + (remained_five // 2))
    # 5의 배수일 경우 5로 나눈 값을 반환
    if remained_five == 0 :
        return cash // 5
    # 5로 나눈 나머지가 홀수일 경우 5원으로 처리 하려 하면 2원으로 나누었을때 0으로 떨어지지 않는다.
    elif remained_five % 2 != 0 :
        # 거슬러 줄 수 없는 1과 3은 예외처리
        if cash == 1 or cash == 3 :
            return -1
        # 2원 계산 식 -> 5의 나머지 값에 5를 더해 2로 나눈다.
        # 5원 계산 식 -> 5로 나눈 값에서 1을 뺀다.
        else : 
            return (cash // 5 - 1) + ((remained_five + 5) // 2)
    # 5로 나눈 나머지가 짝수일 경우 5원으로 나눈 최소 값을 구하고 나머지에 2를 나누어도 0으로 떨어진다.
    else :
        return change_formula

main()


# solution2
def main():
    cash = int(input())
    print(greedy_solution(cash))

def greedy_solution(cash : int) :
    cnt_change = 0
    while True :
        # 손님의 금액이 5의 배수이면 
        if cash % 5 == 0 :
            cnt_change += cash // 5
            break
        # 5의 배수가 안되면 2를 빼고 다시 계산
        else : 
            cnt_change += 1
            cash -= 2
    # 금액이 0보다 작아지면
    if cash < 0 :
        return -1
    #그게 아니라면
    else :
        return cnt_change

main()

'''
1 = 0
2 = t,1
3 = 0
4 = t,2
5 = f,1
6 = t,3
7 = f,1 t,1
8 = t,4
9 = f,1 t,2
10 = f,2
11 = f,1 t,3
12 = f,2 t,1
13 = f,1 t,4
14 = f,2 t,2
15 = f,3
16 = f,2 t,3
17 = f,2 t,2


'''


