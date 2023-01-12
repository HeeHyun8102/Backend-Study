def solution(jobs):
    start = [z for x in jobs for y,z in enumerate(x) if y==0]
    total = sorted([sum(x) for x in jobs])
    
    return 