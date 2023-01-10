import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
       int[] answer = {};  
       ArrayList<Integer> list = new ArrayList<Integer>();
        
       int tempNum=10; 
    
        for(int n: arr){
            if(tempNum !=n) list.add(n);
            tempNum = n;
        }
        
        answer = new int[list.size()];
        for(int i=0; i<answer.length; i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}
