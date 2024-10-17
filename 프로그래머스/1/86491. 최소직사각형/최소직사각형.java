class Solution {
    public int solution(int[][] sizes) {
        int w = 0, h = 0;
        for (int[] card : sizes) {
            w = Math.max(w, Math.max(card[0], card[1]));
            h = Math.max(h, Math.min(card[0], card[1]));
        }
        int answer = w * h;
        return answer;
    }
}