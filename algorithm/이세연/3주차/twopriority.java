import java.util.*;
import java.util.Collections;

class Solution {
    public int[] solution(String[] operations) {
      int[] answer = {0,0};    //큐가 비어있으면 [0,0]으로 출력
        
   PriorityQueue<Integer> minQ = new PriorityQueue();  //최소힙
   PriorityQueue<Integer> maxQ = new PriorityQueue(Collections.reverseOrder()); //최대힙
        
  for(String op : operations){
    //1. 숫자 삽입하는 경우
    if(op.substring(0,1).equals("I")){
          int val = Integer.parseInt(op.substring(2));
          minQ.add(val); 
          maxQ.add(val);
      }
      else if(!minQ.isEmpty()){
          //2. 큐에서 최댓값 삭제하는 경우
          if(op.equals("D 1")){
              int val = maxQ.poll();  
              minQ.remove(val);
          }
          //3. 큐에서 최솟값 삭제하는 경우
          else if(op.equals("D -1")){
              int val = minQ.poll();  
              maxQ.remove(val);
          }
      }
  }
        //값이 있는 경우 [최댓값,최솟값]순으로 출력
        if(!minQ.isEmpty()){
            answer[0] = maxQ.peek(); 
            answer[1] = minQ.peek();
        }
        return answer;
    }
}

//<방법2>
// for(int i = 0; i < operations.length; i++) {
//     String[] strs = operations[i].split(" ");
//     if(strs[0].equals("I")) {
//         minQueue.offer(Integer.valueOf(strs[1]));
//         maxQueue.offer(Integer.valueOf(strs[1]));
//     } else if(strs[0].equals("D") && strs[1].equals("1") && !maxQueue.isEmpty()) {
//         minQueue.remove(maxQueue.poll());
//     } else if(strs[0].equals("D") && strs[1].equals("-1") && !minQueue.isEmpty()) {
//         maxQueue.remove(minQueue.poll());
//     }
// }

// int min = minQueue.isEmpty() ? 0 : minQueue.poll(),
//     max = maxQueue.isEmpty() ? 0 : maxQueue.poll();

// return new int[]{max, min} ;

//<방법3>
//switch-case문으로 해결가능


