void swap (int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
void print(int array[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        printf("%d\t", array[i]);
    }
    printf("\n"); 
}

void rearrange(int array[], int size, int mid, int high) 
{
    int i = 0;
    int j = 0;
    int k = size - 1;
    
    while (j <= k) {
        if (array[j] < mid) {
            swap(&array[i], &array[j]);
            i++;
            j++;
        } else if (array[j] > high) {
            swap(&array[j], &array[k]);
            k--;
        } else {
            j++;
        }
    }
    printf("i:%d, j:%d, k:%d\n", i,j,k);
}

void rearrange1(int array[], int size, int mid, int high) 
{
    int i;
    int k = 0;
    for (i = 0; i < size; i++) {
        if (array[i] < mid) {
            swap(&array[k++], &array[i]);
        }
    }
    for (i = k; i < size; i++) {
        if (array[i] >= mid && array[i] <= high) {
            swap(&array[k++], &array[i]);
        }
    }
}  
  
static int array[] = {2, 6, 1, 4, 3, 5, 3, 4, 7, 6, 8, 9, 10};

int main() {
    int size = sizeof(array)/sizeof(array[0]);
    print(array, size);
    rearrange1(array, size, 4, 6);
    print(array, size);
    return 0;
}