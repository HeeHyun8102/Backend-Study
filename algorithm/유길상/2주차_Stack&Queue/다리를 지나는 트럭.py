from collections import deque

def solution(bridge_length, weight, truck_weights):
    tot_sec = 0
    boarding = deque(bridge_length * [0])
    waiting = deque(truck_weights)
    on_weight = 0
    while len(boarding):
        tot_sec += 1
        print("bording -> ", boarding)
        boarding.popleft()
        if waiting: # 기다리는 트럭이 있으면.
            if weight >= sum(boarding) + waiting[0]: # 다리가 버틸 수 있는 무게라면
                boarding.append(waiting.popleft()) # 기다리는 트럭 왼쪽을 지나가는 트럭으로 넣어주기
            else :
                boarding.append(0)
    return tot_sec

print(solution(2, 10, [7,4,5,6]))