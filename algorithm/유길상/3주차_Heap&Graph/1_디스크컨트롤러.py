import heapq

#def solution(jobs):   
#    heap = []
##    wait, chk_sec, start_point = 0, 0, 0
#    for i in jobs:
#        heapq.heappush(heap, [i[1],i[0]])
#    heap.sort()#

#    while heap:
#        is_working = True
#        while is_working:
#            chk_sec += 1
#            if chk_sec == heap[0][0]:
###                start_point = int(chk_sec - heap[0])
#                heapq.heappop(heap)
#                chk_sec = 0
#                is_working = False
        
        
    
    

#    return 



import heapq

def solution(jobs):   
    answer, now, i = 0, 0, 0
    start_time = -1
    heap = []
    while i < len(jobs):  #작업한 양이 jobs보다 작을 동안
        for j in jobs:
            if start_time < j[0] <= now: # 작업 시작시간보다 크고 현재 시간보다 같거나 작으면
                heapq.heappush(heap, [j[1], j[0]]) # 정렬
        if len(heap) > 0: # 힙의 길이가 0보다 크면, 작업할게 있으면
            current = heapq.heappop(heap) # 최근에 작업한 내용
            start_time = now # 작업 시작 시간을 현재시간으로
            now += current[0] # 현재시간에 최근 작업시간을 더한다.
            answer += (now - current[1]) # 현재 시간에서 작업 시작 시간을 뺀 후 더해준다
            i += 1
            print(i)
        else:
            now += 1
    return int(answer / len(jobs))


par = [[0,3],[1,9],[2,6]]

print(solution(par))