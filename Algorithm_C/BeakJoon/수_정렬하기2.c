#include <stdio.h>

int array[1000001];

void quickSort(int* data, int start, int end) {
    if (start >= end)
        return;

    int pivot = start;
    int i = start + 1;
    int j = end;
    int temp;

    while (i <= j) {

        while (data[i] <= data[pivot])
            i++;
        while (data[j] >= data[pivot] && j > start)
            j--;

        if (i > j) {
            temp = data[j];
            data[j] = data[pivot];
            data[pivot] = temp;
        }

        else {
            temp = data[i];
            data[i] = data[j];
            data[j] = temp;
        }

        quickSort(data, start, j - 1);
        quickSort(data, j + 1, end);
    }

 
    return;
}

int main(void) {

    int i, num;

    scanf_s("%d", &num);

    for (i = 0; i < num; i++)
    {
        scanf_s("%d ", &array[i]);
    }

    quickSort(array, 0, num - 1);

    for (i = 0; i < num; i++) {
        printf("%d ", array[i]);
    }

    return 0;
}