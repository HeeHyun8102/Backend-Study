'''
1. 총 플레이가 가장 높은 노래 장르를 먼저 고른다. most_play += plays[genres]
2. 총 플레이가 높은 노래 장르에서 가장 많이 플레이 된 곡을 고른다. max(play.get(genres))
3. 고른 장르안에서 플레이 된 횟수가 같은 노래는 고유 번호가 낮은 노래를 먼저 고른다. if play[i] == play[i+1]: return play[i]
'''

def solution(genres, plays):
    answer = []
    gen_tot = {} # 장르를 key값으로 장르에 대한 총 플레이 수 집계
    all_list = {} # 플레이 수를 key값으로 딕셔너리 생성
    index = 0
    
    # 총 플레이가 가장 높은 노래 장르 추출하기
    for gen, num in zip(genres, plays):
        all_list[index] = gen, num #장르, 플레이수 리스트 키 : 밸류 , 고유번호로 딕셔너리 생성
        index += 1
        if gen not in gen_tot.keys():
            gen_tot[gen] = num
        else :
            gen_tot[gen] += num
    
    # 총 플레이가 높은 노래 장르 정렬하기.
    sorted_gen_tot = sorted(gen_tot.items(), key = lambda x: x[1], reverse=True)
    
    #전체 딕셔너리에서 정렬
    

    # 총 플레이가 높은 노래 장르를 기준으로 길이가 2만큼만 고유번호를 리턴 변수에 append 해주기
    for gen, num in sorted_gen_tot:
        sorted_all_list = sorted(all_list[gen],key = lambda x: (x[1],-x[0]), reverse=True)
        for i in range(2):
            if gen == sorted_all_list[0][1][0]:
                answer.append(sorted_all_list[0][0])
                sorted_all_list.pop([0][0]) # 삭제 
            for i in range(len(sorted_all_list)):# 리턴 값에 넣어 준 후 해당 장르 음악이 남아있다면 삭제
                if gen in sorted_all_list[0][1][0]:
                    sorted_all_list.pop([0][0])
                else:
                    continue

    return answer