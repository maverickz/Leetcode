#include <stdio.h>

int fibonacci_recur(int n)
{
    if (n < 0) {
        return -1;
    } else if (n == 1) {
        return 0;
    } else if (n <= 3) {
        return 1;
    } else {
        return fibonacci_recur(n-1) + fibonacci_recur(n-2);
    }
}

int fibonacci_iter(int n)
{
    if (n < 0) {
        return -1;
    } else if (n == 1) {
        return 0;
    } else if (n <= 3) {
        return 1;
    } else {
        int i;
        int f0 = -1;
        int f1 = 1;
        int f2 = f0 + f1;
        for (i = 0; i < n; i++) {
            f2 = f0 + f1;
            f0 = f1;
            f1 = f2;
        }
        return f2;
    } 
}

int main()
{
    int num = 4;
    printf("%d\n", fibonacci_iter(11));
    return 0;
}
