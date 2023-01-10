import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = false;

        Stack<Character> stack = new Stack<>();
        
        if(s.charAt(0) == ')') return false;  
        
        for(int i=0; i<s.length(); i++){ 
            if(s.charAt(i) == '('){ 
                stack.push(s.charAt(i)); 
            }else{ //')'괄호인경우, 
                if(!stack.isEmpty() && s.charAt(i) == ')')
                    stack.pop();
            }
        }
        
        if(stack.isEmpty()){
            answer=true;
        }
     return answer;   
    }
}
