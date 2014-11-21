#include <stdio.h>
#include <stdlib.h>

void print_array(int array[], int len)
{
    int i;
    printf("[ ");
    for (i = 0; i < len; i++) { 
        printf("%d ", array[i]); 
    }
    printf("]\n");
}

void copy(int A[], int B[], int start, int end)
{
    int i = 0;
    int j = 0;
    for (i = start, j = 0; i <= end; i++, j++) {
        B[j] = A[i];
    }
}

void merge(int array[], int l_start, int l_end, int r_start, int r_end)
{
    int i;
    int j;
    int k = 0;
    int l_len = l_end - l_start + 1;
    int r_len = r_end - r_start + 1;
    int *left = calloc(1, l_len * sizeof(int));
    int *right = calloc(1, r_len * sizeof(int));
    copy(array, left, l_start, l_end);
    copy(array, right, r_start, r_end);

    for (i = 0, j = 0, k = l_start; i < l_len && j < r_len; k++) {
        if (left[i] < right[j]) {
            array[k] = left[i];
            i++;
        } else {
            array[k] = right[j];
            j++;
        }
    }

    for (; i < l_len; i++, k++) {
        array[k] = left[i];
    }

    for (; j < r_len; j++, k++) {
        array[k] = right[j];
    }

    free(left);
    free(right);
}

void merge_sort(int array[], int start, int end)
{
    if ((end - start) < 1) {
        // A single element is assumed to be sorted
        return;
    }

    int mid = start + (end - start) / 2;
    merge_sort(array, start, mid);
    merge_sort(array, mid + 1, end);
    merge(array, start, mid, mid + 1, end);
}

int main()
{
    int array[15] = { 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 };
    int len = 15;
    print_array(array, len);
    merge_sort(array, 0, len - 1);
    print_array(array, len);
}