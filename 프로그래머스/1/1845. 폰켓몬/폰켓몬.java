import java.util.Arrays;

class Solution {
    public int solution(int[] nums) {
        int[] lst = Arrays.stream(nums).distinct().toArray();
        return Math.min(nums.length / 2, lst.length);
    }
}