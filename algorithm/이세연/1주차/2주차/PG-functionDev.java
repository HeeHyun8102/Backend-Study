import java.util.*; 

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
       
        Queue<Integer> queue = new LinkedList<>(); 
        
        for(int i=0; i<progresses.length; i++){
            queue.add((int) Math.ceil((100.0-progresses[i]) / speeds[i]));
        }
        
    
        ArrayList<Integer> result = new ArrayList<>();
        while(!queue.isEmpty()){
            int day = queue.poll(); 
            int cnt = 1;
            
            while(!queue.isEmpty() && day >= queue.peek()){
                cnt++;
                queue.poll();//큐 맨 앞에 있는 값 반환 후 삭제
            }
            result.add(cnt);
        }
        
        int[] answer = new int[result.size()];
        for (int i=0; i<result.size(); i++){
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}

