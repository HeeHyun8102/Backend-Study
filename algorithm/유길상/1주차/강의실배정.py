lecture = int(input())
time = [list(map(int, input().split())) for _ in range(lecture)]
temp = sorted(time)
time.sort

for first in range(lecture) :
    for next in range(first+1, lecture) :
        if next < len(temp) and time[first][1] <= temp[next][0] and first != next:
            temp[first] = temp[next] # push
            temp.remove(temp[next]) # pop
            break

print(len(temp))