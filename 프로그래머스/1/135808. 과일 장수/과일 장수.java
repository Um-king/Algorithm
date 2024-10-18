import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        // 오름차순 정렬
        Arrays.sort(score);
        
        // 내림차순 정렬
        for(int i=0; i<score.length / 2; i++) {
            int temp = score[i];
            score[i] = score[score.length-1-i];
            score[score.length-1-i] = temp;
        }
        
        for(int i=0; i<score.length/m; i++) {
            int[] arr = Arrays.copyOfRange(score, m*i, m*(i+1));
            answer += arr[arr.length - 1] * m;
        }
        return answer;
    }
}