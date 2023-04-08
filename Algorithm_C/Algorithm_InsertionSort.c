/*
## [삽입 정렬]
## 다음의 숫자들을 오름차순으로 정렬하는 프로그램 작성
   1 10 5 8 7 6 4 3 2 9

   : 삽입정렬은 n^2만큼 비교연산 소요 => "삽입정렬의 시간 복잡도는 O(N^2)"
   : 거의 정렬된 상태라면 가장 효율적이다.
   */


#include <stdio.h>

int main(void) {
	int i, j, temp;
	int array[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

	for (i = 0; i < 9; i++) {
		j = i;
		while (array[j] > array[j + 1]) {
			temp = array[j];
			array[j] = array[j + 1];
			array[j + 1] = temp;
			j--;
		}
	}

	for (i = 0; i < 10; i++)
		printf("%d ", array[i]);
	return 0;
}