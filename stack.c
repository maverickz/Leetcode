#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int *bottom = NULL;
int *top = NULL;
int size = 0;

bool stack_full() 
{
	return (bottom + size) == top;
}

bool stack_empty()
{
	return bottom == top;
}

void create_stack(int size_)
{
    size = size_;
    int *tmp = calloc(1, sizeof(int)*size_);
    if (tmp) {
        bottom = top = tmp;
    }
}

void push(int value)
{
	if (stack_full()) {
        printf("Error: Stack is full, cannot push %d\n", value);
        return;
    } else {
        *top = value;
        top++;
    }
}

int pop()
{
    if (stack_empty()) {
        printf("Error: Stack is empty\n");
        return -1;
    } else {
        top--;
        int value = *top;
        return value;
    }
}

int peek()
{
    if (stack_empty()) {
        printf("Error: Stack is empty\n");
        return -1;
    } else {
        int value = *(top-1);
        return value;
    }
}

int main()
{
    int stack_size = 5;
    int i;
    create_stack(stack_size);
    for (i = 0; i <= stack_size; i++) {
        push(i+1);
    }

    printf("Peek into stack: %d\n", peek());

    for (i = 0; i <= stack_size; i++) {
        int value = pop();
        printf("Value popped: %d\n", value);
    }

    return 0;
}


