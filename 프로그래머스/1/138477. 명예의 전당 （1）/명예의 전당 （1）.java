import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        List<Integer> result = new ArrayList<Integer>();
        int[] answer = new int[score.length];
        
        for(int i=0; i<score.length; i++) {
            result.add(score[i]);
            if(result.size() > k) {
                result.remove(Integer.valueOf(Collections.min(result)));
            }
            answer[i] = Collections.min(result);
        }
        
        return answer;
    }
}