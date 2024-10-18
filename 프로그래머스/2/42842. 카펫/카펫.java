import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        List<Integer> lst = new ArrayList<>();
        int[] answer = new int[2];
        int num = brown + yellow;
        
        for(int i=1; i<=num; i++) {
            if (num % i == 0)
                lst.add(i);
        }
    
        for(int h : lst) {
            int w = num / h;
            if((w-2) * (h-2) == yellow) {
                answer[0] = w;
                answer[1] = h;
                
                break;
            }
        }
        return answer;
    }
}