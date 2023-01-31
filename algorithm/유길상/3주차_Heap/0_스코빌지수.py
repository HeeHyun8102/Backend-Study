import heapq

def solution(scoville, K):
    result = 0
    heapq.heapify(scoville) # 힙으로 변환
    try:
        while scoville[0] < K: # 최소값이 K보다 작은동안 반복        
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)) # 힙scoville에 새로운 매운 맛 원소 추가
            result += 1 # 더한 값
    except IndexError: return -1 # 원소 값이 없으면 -1 리턴
    else : return result

solution([1, 2, 3, 9, 10, 12],7)


