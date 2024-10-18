class Solution {
    public String solution(String s, int n) {
        String answer = "";
        int asciiValue = 0;
        
        for(char c : s.toCharArray()) {
            if (c == ' ') {
                answer += c;
            }
            else if(Character.isUpperCase(c)) {
                asciiValue = ((int) c - (int) 'A' + n) % 26 + (int) 'A';
                answer += (char) asciiValue;
            }
            else if (Character.isLowerCase(c)) {
                asciiValue = ((int) c - (int) 'a' + n) % 26 + (int) 'a';
                answer += (char) asciiValue;
            }
        }
        
        return answer;
    }
}