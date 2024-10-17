class Solution {
    boolean solution(String s) {
        int cnt = 0;
        String str = s.toLowerCase();
            
        for(char c : str.toCharArray()) {
            if(c == 'p')
                cnt++;
            else if (c == 'y')
                cnt--;
        }

        return cnt == 0;
    }
}