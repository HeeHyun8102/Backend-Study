def solution(clothes):
    dic = dict(clothes)
    category = set(dic.values()) # 의상 종류 중복 제거
    item = list(dic.keys()) # 의상 이름
    overlab = len(item) - len(category) + 1
    cnt = 0
    if len(category) == 1:
        return len(item)
    print(len(category))
    for j in range(0,len(category)):
        for k in range(j+1, len(category)):
            print("j= ",j,"일때")
            print(k)
            cnt += 1
    print(cnt)
    return (cnt*overlab) + len(item)

#clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [
    ["yellow_hat", "headgear"],
    ["red_hat", "headgear"],
    ["blue_shirts", "shirts"],
    ["red_shirts", "shirts"],
    ["jean", "pants"],
    ["long_coat", "outer"],
]

print(solution(clothes))