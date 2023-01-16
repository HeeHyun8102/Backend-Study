import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
    
    int answer = 0;  
    PriorityQueue<Integer> pq = new PriorityQueue<>();

    //1. 스코빌 지수가 담긴 배열을 우선순위 큐에 담는다
    for(int i : scoville){
		pq.offer(i);
    }

    while(pq.peek() < K) //pq.peek()한 값이 K보다 크면 종료
    {   
        if(pq.size() ==1) {
            return -1; //예외처리
        }
        
        int first_not_spicy = pq.poll();
        int second_not_spicy = pq.poll();

        int result = first_not_spicy + (second_not_spicy*2);

        pq.offer(result);
        answer++;
    }

        return answer;
    }
}
