/*
## [퀵 정렬]
## 다음의 숫자들을 오름차순으로 정렬하는 프로그램 작성
   1 10 5 8 7 6 4 3 2 9

   : "퀵정렬의 평균 시간 복잡도는 O(N*logN)" 
   최악의 경우 시간복잡도는 O(N^2) -> 이미 정렬이 되어 있는 경우
   */


#include <stdio.h>

int number = 10;
int data[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

/// <summary>
/// 퀵정렬 수행 함수
/// </summary>
/// <param name=""></param>
/// <returns></returns>
void quickSort(int* data, int start, int end) {
	if (start >= end) { // 원소가 1개인 경우
		return;
	}

	int pivot = start; // 피벗값 설정: 첫번째 원소
	int i = start + 1;
	int j = end;
	int temp;

	while (i <= j) { // 엇갈릴 때까지 반복
		while (data[i] <= data[pivot]) { // 피벗값 보다 큰 값을 만날때 까지
			i++;
		}
		while (data[j] >= data[pivot] && j > start) { // 피벗값 보다 작은 값을 만날때 까지
			j--;
		}
		if (i > j) { // 현재 엇갈린 상태면 피벗값과 교체
			temp = data[j];
			data[j] = data[pivot];
			data[pivot] = temp;
		}
		else { // 엇갈리지 않았다면 큰값과 작은 값을 변경
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
	}

	// 키값을 기준으로 오른쪽과 왼쪽 퀵정렬 수행
	quickSort(data, start, j - 1);
	quickSort(data, j + 1, end);
}

int main(void) {
	quickSort(data, 0, number - 1);
	for (int i = 0; i < number; i++) {
		printf("%d ", data[i]);
	}

	return 0;
}