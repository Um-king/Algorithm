import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        List<Integer> stack = new ArrayList<>();
        
        
        for(int i : moves) {
            for(int j = 0; j < board.length; j++){
                if(board[j][i-1] != 0) {
                    stack.add(board[j][i-1]);
                    board[j][i-1] = 0;
                    
                    if (stack.size() > 1) {
                        if (stack.get(stack.size()-1) == stack.get(stack.size()-2)) {
                            stack.remove(stack.size()-1);
                            stack.remove(stack.size()-1);
                            answer += 2;
                        }
                    }
                    break;                    
                }
            }
        }
        
        return answer;
    }
}