from collections import deque

def solution(bridge_length, weight, truck_weights):
    tot_sec = 1
    bording = deque(bridge_length * [0])
    waiting = deque(truck_weights)
    arrive = deque(len(truck_weights) * [0])
    on_weight = 0
    cnt = 0
    while 0 in arrive:
        tot_sec += 1
        cnt += 1
        if waiting:
            if weight <= on_weight:
                on_weight -= waiting[0]
            elif weight > on_weight: 
                on_weight += waiting[0]
                bording.append(waiting.popleft())
                waiting.append(0)
            if cnt == bridge_length:
                arrive.append(bording[0])
                arrive.popleft()
                on_weight -= bording.popleft()
                cnt -= 1
    return tot_sec