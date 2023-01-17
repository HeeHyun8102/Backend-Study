import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        
        //1. 요청시간에 따른 오름차순 정렬
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        
        //2. 소요시간에 따른 오름차순 정렬 
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        int index = 0; // jobs 배열의 인덱스
        int count = 0; // 수행된 요청 갯수
        int total = 0; // 요청에서 종료까지의 최소합
        int end = 0; // 수행되고난 직후의 시간

        while(count < jobs.length) { 
            
            while(index < jobs.length && jobs[index][0] <= end) {
                pq.add(jobs[index++]);
            }
            
            if(pq.isEmpty()) {
                end = jobs[index][0];
            } else {
                int[] cur = pq.poll();
                total += cur[1] + end - cur[0];
                end += cur[1];
                count++;
            }
        }

        answer = total / jobs.length;
        return answer;
    }
}
