/*
## [선택 정렬]
## 다음의 숫자들을 오름차순으로 정렬하는 프로그램 작성
   1 10 5 8 7 6 4 3 2 9

   : 선택정렬은 n^2만큼 비교연산 소요 => "선택정렬의 시간 복잡도는 O(N^2)"
*/


#include <stdio.h>

int main(void) {
	int i, j, min, index, temp;
	int array[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

	for (i = 0; i < 10; i++) {
		min = 9999;
		for (j = i; j < 10; j++) {
			if (min > array[j]) {
				min = array[j];
				index = j;
			}
		}
		temp = array[i];
		array[i] = array[index];
		array[index] = temp;
	}
	
	for (i = 0; i < 10; i++)
		printf("%d ", array[i]);
	return 0;
}