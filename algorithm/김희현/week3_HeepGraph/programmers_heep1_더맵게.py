# runtime error
def solution(scoville, k):
    s = sorted(scoville)
    
    if k > 0 and set(s) == {0}:
        answer = -1
        return answer
    else:
        answer = 0
        while s[0] < k:
            answer += 1
            n = s[0] + s[1]*2
            del s[0:2]
            s.append(n)
            s = sorted(s)
        
        return answer