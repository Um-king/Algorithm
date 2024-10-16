import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        // 문자열 배열로 변환
        String[] strNumbers = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .toArray(String[]::new);
        
        // 정렬 기준 정의: (a + b)와 (b + a)를 비교하여 내림차순 정렬
        Arrays.sort(strNumbers, new Comparator<String> () {
            @Override
            public int compare(String a, String b) {
                return (b + a).compareTo(a + b);
            }
        });
        
        // 내림 차순 후 첫 원소가 0인 경우는 모든 원소가 0인 경우
        if(strNumbers[0].equals("0")) {
            return "0";
        }
        
        // 정렬된 문자열 연결
        for (int i = 0; i < strNumbers.length; i++) {
            answer = answer + strNumbers[i];
        }
        
        return answer;
    }
}