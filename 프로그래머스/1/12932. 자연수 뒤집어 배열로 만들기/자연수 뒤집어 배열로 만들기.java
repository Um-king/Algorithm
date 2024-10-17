import java.util.*;

class Solution {
    public int[] solution(long n) {
        ArrayList<Integer> answer = new ArrayList<>();
        String num = Long.toString(n);
        
        for(int i = 0; i < num.length(); i++) {
            answer.add(Integer.parseInt(String.valueOf(num.charAt(i))));
        }
        
        Collections.reverse(answer);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}