#def solution(participant, completion):
#    index = 0
#    while len(participant) > 1:
#        if index >= len(participant):
#            index = 0
#        if participant[index] == completion[-1]:
#            completion.pop()
#            participant.pop(index)
#        index += 1
#    cant_completion = participant[0]
#    
#    return cant_completion

#def solution(participant, completion):
#    participant.sort()
#    completion.sort()

#    while len(participant) > 1:
#        if participant[0] == completion[0]:
#            answer = {participant.pop(0) : completion.pop(0)}
#        else:
#            return participant.pop(0)
#    return participant.pop(0)

def solution(participant, completion):
    answer = ''
    hash = {}
    answer = participant[0]    

    return answer
    

participant = 	["mislav", "stanko", "mislav", "ana"]#["marina", "josipa", "nikola", "vinko", "filipa"]#["leo", "kiki", "eden"]
completion =  ["stanko", "ana", "mislav"]#["josipa", "filipa", "marina", "nikola"]#["eden", "kiki"]

print(solution(participant,completion))
#solution(participant,completion)