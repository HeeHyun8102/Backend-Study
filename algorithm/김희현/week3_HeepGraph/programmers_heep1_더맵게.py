# 첫 번째 시도
# 시간 초과
def solution(scoville, k):
    s = sorted(scoville)
    
    if k > 0 and set(s) == {0}:
        answer = -1
        return answer

    else:
        answer = 0
        while s[0] < k:
            try:
                answer += 1
                n = s[0] + s[1]*2
                del s[0:2]
                s.append(n)
                s = sorted(s)

            except IndexError:
                answer = -1
                return answer
        
        return answer

# 해결
# 두 번째 시도
# heapq : 최소힙 모듈
# heapify(list) : list를 heap으로 자동 변환
# heapush(heap,item) : heap에 item을 추가
# heappop(heap) : heap에서 가장 작은 요소를 반환 후 삭제
from heapq import heapify, heappush, heappop

def solution(s, k):
    if k > 0 and set(s) == {0}:
        return -1
    
    else:
        heapify(s)
        answer = 0
        while s[0] < k:
            try:
                answer += 1
                n = heappop(s) + heappop(s)*2
                heappush(s,n)
            
            except IndexError:
                return -1
        
        return answer
            

# 고수분들의 코드
#1
from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapify(scoville)
    for i in range(1000000):
        try:
            heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
            if scoville[0] >= K: return i+1
        except:
            return -1

#2
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
        

