#include <stdio.h>
#include <string.h>

void swap (char *x, char *y)
{
    char temp = *x;
    *x = *y;
    *y = temp;
}

void string_permute(char *str, int start, int end)
{
    if (start == end) {
        printf("%s\n", str);
    } else {
        int i = start;
        int j;
        for (j = i; j < end; j++) {
            swap(str+i, str+j);
            string_permute(str, i+1, end);
            // When we reach a leaf of the given tree, 
            // the leaf is printed. To get back to the other strings i.e other leaves, 
            // we have to backtrack.
            swap(str+i, str+j);
        }
    }
}


char sample[] = {"abcd"};
int main()
{
    string_permute(sample, 0, 4);
    return 0;
}