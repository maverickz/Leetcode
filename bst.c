#include <stdio.h>
#include <stdlib.h>

typedef struct tree_node_s {
    int value;
    struct tree_node_s *left;
    struct tree_node_s *right;
} tree_node_t;

void inorder(tree_node_t *root) {
    if (!root) {
        return;
    }
    inorder(root->left);
    printf("%d [%d, %d]\n", root->value, root->left?root->left->value:0, root->right?root->right->value:0);
    inorder(root->right);
}

tree_node_t *insert(tree_node_t *root, int value)
{
    if (root == NULL) {
        tree_node_t *new_node = calloc(1, sizeof(tree_node_t));
        new_node->value = value;
        root = new_node;
    } else if (root->value > value) {
        root->left = insert(root->left, value);
    } else {
        root->right = insert(root->right, value);
    }
    return root;
}

tree_node_t *search(tree_node_t *root, int value)
{
    if (!root) {
        return NULL;
    } else if (root->value > value) {
        return search(root->left, value);
    } else if (root->value < value) {
        return search(root->right, value);
    } else {
        return root;
    }
}

tree_node_t *find_min_node(tree_node_t *root)
{
    tree_node_t *curr_node = root;
    while (curr_node->left) {
        curr_node = curr_node->left;
    }
    return curr_node;
}


tree_node_t *delete(tree_node_t *root, int value) 
{
    if (root == NULL) {
        return root;
    } else if (root->value > value) {
        root->left = delete(root->left, value);
    } else if (root->value < value) {
        root->right = delete(root->right, value);
    } else {
        if (root->left && root->right) {
            tree_node_t *successor = find_min_node(root->right);
            root->value = successor->value;
            root->right = delete(root->right, root->value);
        } else {
            tree_node_t *tmp = root;
            if (root->left == NULL) {
                root = root->right;
            } else if (root->right == NULL) {
                root = root->left;
            } 
            free(tmp);
        }
    }
    return root;  
}


void display(tree_node_t *root, int array[], int n)
{
    int i;
    printf("*******************************************************\n");
    for (i = 0; i < n; i++) {
        tree_node_t *node = search(root, array[i]);
        printf ("Key: %d, Value:%d, Address:%p\n", array[i], node?node->value:-1, node);
    }
    printf("*******************************************************\n");
}

int main()
{

    int i;
    int sample_data[] = {8,3,10,1,6,14,4,7,13};
    int len = sizeof(sample_data)/sizeof(sample_data[0]);
    tree_node_t *root = NULL;
    for (i = 0; i < len; i++) {
        root = insert(root, sample_data[i]);
    }
    for (i = 0; i < 4; i++) {
        int index = rand() % len;
        root = delete(root, sample_data[index]);
    }
    inorder(root);
    return 0;
}