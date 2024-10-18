import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {

        List<String> card1 = new ArrayList<>(Arrays.asList(cards1));
        List<String> card2 = new ArrayList<>(Arrays.asList(cards2));
        
        for(int i=0; i<goal.length; i++) {
            if(card1.contains(goal[i]) && card1.get(0).equals(goal[i])){
                card1.remove(0);
            }
            else if(card2.contains(goal[i]) && card2.get(0).equals(goal[i])){
                card2.remove(0);
            }
            else {
                return "No";
            }
        }
        
        
        return "Yes";
    }
}