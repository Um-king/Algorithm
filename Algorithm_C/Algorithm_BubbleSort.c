/*
## [버블 정렬]: 옆에 있는 값과 비교하여 이동
## 다음의 숫자들을 오름차순으로 정렬하는 프로그램 작성
   1 10 5 8 7 6 4 3 2 9

   : 버블정렬은 n^2만큼 비교연산 소요 => "버블정렬의 시간 복잡도는 O(N^2)"
*/


#include <stdio.h>

int main(void) {
	int i, j, temp;
	int array[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

	for (i = 0; i < 10; i++) {
		for (j = 0; j < 9 - i; j++) {
			if (array[j] > array[j + 1]) {
				temp = array[j + 1];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}

	for (i = 0; i < 10; i++)
		printf("%d ", array[i]);
	return 0;
}