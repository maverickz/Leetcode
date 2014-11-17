#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node {
 char *word;
 struct node *next;
} node;

#define HASH_SIZE 512
#define NHASH 5
#define MULT 31
node *hash_table[HASH_SIZE];

unsigned int hash(char *p) 
{
	unsigned int h = 0;
	for ( ; *p; p++) {
		h = MULT * h + *p;
	}
	return h % HASH_SIZE;
}

char *get(char *key)
{
	unsigned int h = hash(key);
	node *p = hash_table[h];
	if (p != NULL) {
		return p->word;
	} else {
		return NULL;
	}
}

void put(char *key, char *value)
{
	unsigned int h = hash(key);
	printf ("Key:%s, hash:%d\n", key, h);
	node *p = NULL;

	for (p = hash_table[h]; p != NULL; p = p->next) {
		if (strcmp(value, p->word) == 0) {
			return;
		}
	}
	
	p = (node *)malloc(sizeof(node));
	p->word = strdup(value);
	p->next = hash_table[h];
	hash_table[h] = p;
}

int main()
{
	int i;
	char *keys[NHASH] = {"one","two","three","four","five"};
	char *values[NHASH] = {"val1","val2","val3","val4","val5"};

	for (i = 0; i < NHASH; i++) {
		hash_table[i] = NULL;
	}
	
	for (i = 0; i < NHASH; i++) {
		put(keys[i], values[i]);
	}

    printf("******************GET******************\n");
	for (i = 0; i < NHASH; i++) {
		char *value = get(keys[i]);
		printf("Key: %s, value:%s\n", keys[i], value);
	}
	return 0;
}
