#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) 
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void print_array(int array[], int len)
{
    int i;
    printf("[ ");
    for (i = 0; i < len; i++) { 
        printf("%d ", array[i]); 
    }
    printf("]\n");
}

int partition(int array[], int start, int end)
{
    int num_elem = end - start + 1;
    int pivot_index = rand() % num_elem + start;
    int pivot = array[pivot_index];
    swap(&array[pivot_index], &array[end]);
    int i;
    int j = start;
    for (i = start; i <= end; i++) {
        if (array[i] < pivot) {
            swap(&array[i], &array[j]);
            j++;
        }
    }
    swap(&array[j], &array[end]);
    return j;
}

void quick_sort(int array[], int start, int end)
{
    if (start < end) {
        int p = partition(array, start, end);
        quick_sort(array, 0, p - 1);
        quick_sort(array, p + 1, end);
    }
}

int main()
{
    int array[15] = { 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 };
    int len = 15;
    print_array(array, len);
    quick_sort(array, 0, len - 1);
    print_array(array, len);
}