#include <stdio.h>

int main()
{
    FILE *fp = NULL;
    fp = fopen("sample.txt", "r");
    if (!fp) {
        return 0;
    }
    int val;
    char char_val[2];
    while (!feof(fp)) {
        if (!fscanf(fp, "%d ", &val)) {
            fscanf(fp, "%s ", char_val);
            printf("Char: %s\n", char_val);
            break;
        } else {
            printf("Num: %d\n", val);
        }
    }
    return 0;
}