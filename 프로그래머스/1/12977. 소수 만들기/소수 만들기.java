import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        List<Integer> lst = new ArrayList<>();
        
        for(int i=0; i<nums.length; i++) {
            for(int j=i+1; j<nums.length; j++) {
                for(int k=j+1; k<nums.length; k++) {
                    lst.add(nums[i] + nums[j] + nums[k])  ;          
                }
            }
        }
        
        for(int i : lst) {
            if(isPrime(i))
                answer++;
        }
        
        return answer;
    }
    
    public boolean isPrime(int num) {
        for(int i=2; i<num; i++){
            if(num%i==0)
                return false;
        }
        return true;
    }
}