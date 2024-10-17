
class Solution {
    public int Gcd(int x, int y) {
        int tmp = 0;
        while (y != 0) {
            tmp = y;
            y = x % y;
            x = tmp;
        }
        return x;
    }

    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        int gcd_value = Gcd(n, m);
        int lcm_value = (n * m) / gcd_value;
        answer[0] = gcd_value;
        answer[1] = lcm_value;
        return answer;
    }
}