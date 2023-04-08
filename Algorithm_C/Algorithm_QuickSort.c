/*
## [�� ����]
## ������ ���ڵ��� ������������ �����ϴ� ���α׷� �ۼ�
   1 10 5 8 7 6 4 3 2 9

   : "�������� ��� �ð� ���⵵�� O(N*logN)" 
   �־��� ��� �ð����⵵�� O(N^2) -> �̹� ������ �Ǿ� �ִ� ���
   */


#include <stdio.h>

int number = 10;
int data[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

/// <summary>
/// ������ ���� �Լ�
/// </summary>
/// <param name=""></param>
/// <returns></returns>
void quickSort(int* data, int start, int end) {
	if (start >= end) { // ���Ұ� 1���� ���
		return;
	}

	int pivot = start; // �ǹ��� ����: ù��° ����
	int i = start + 1;
	int j = end;
	int temp;

	while (i <= j) { // ������ ������ �ݺ�
		while (data[i] <= data[pivot]) { // �ǹ��� ���� ū ���� ������ ����
			i++;
		}
		while (data[j] >= data[pivot] && j > start) { // �ǹ��� ���� ���� ���� ������ ����
			j--;
		}
		if (i > j) { // ���� ������ ���¸� �ǹ����� ��ü
			temp = data[j];
			data[j] = data[pivot];
			data[pivot] = temp;
		}
		else { // �������� �ʾҴٸ� ū���� ���� ���� ����
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
	}

	// Ű���� �������� �����ʰ� ���� ������ ����
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